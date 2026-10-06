"""A tiny, dependency-free browser for the Python practice repository."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse
import json
import re

ROOT = Path(__file__).resolve().parent
WEB = ROOT / "web"
NOTES = ROOT / "notes"
GROUPS = {
    "basics": ("Foundations", "01"),
    "data-structures": ("Data structures", "02"),
    "functions": ("Functions", "03"),
    "oop": ("Object-oriented", "04"),
    "problems": ("Coding problems", "05"),
    "projects": ("Projects", "06"),
    "experiments": ("Experiments", "07"),
    "numpy": ("NumPy", "08"),
    "pandas": ("Pandas", "09"),
}


def catalog():
    items = []
    groups = dict(GROUPS)
    # Treat each top-level folder containing Python files as a learning path.
    # This keeps the docs browser ready for libraries added later (for example
    # matplotlib, scikit-learn, or PyTorch) without another server edit.
    known = set(groups)
    for folder in sorted(ROOT.iterdir(), key=lambda path: path.name.casefold()):
        if not folder.is_dir() or folder.name.startswith(".") or folder.name in known:
            continue
        if not any(folder.rglob("*.py")):
            continue
        label = re.sub(r"[-_]", " ", folder.name).title()
        groups[folder.name] = (label, f"{len(groups) + 1:02}")

    for category, (label, order) in groups.items():
        folder = ROOT / category
        if not folder.is_dir():
            continue
        for path in sorted(folder.rglob("*.py")):
            rel = path.relative_to(ROOT).as_posix()
            stem = re.sub(r"^\d+[_\- ]*", "", path.stem).replace("_", " ").replace("-", " ")
            title = re.sub(r"\b\w", lambda m: m.group().upper(), stem)
            items.append({"path": rel, "title": title, "category": category,
                          "categoryLabel": label, "order": order})
    return items


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = urlparse(self.path).path
        if route == "/api/files":
            return self.send_json(catalog())
        if route == "/api/notes":
            files = sorted(NOTES.glob("*.pdf"), key=lambda path: path.name.casefold())
            return self.send_json([{"name": path.name, "title": path.stem.strip(), "size": path.stat().st_size}
                                  for path in files if path.is_file()])
        if route.startswith("/api/notes/"):
            name = unquote(route.removeprefix("/api/notes/"))
            path = NOTES / name
            if path.parent != NOTES or path.suffix.lower() != ".pdf" or not path.is_file():
                return self.send_error(404)
            data = path.read_bytes()
            start, end, status = 0, len(data) - 1, 200
            byte_range = self.headers.get("Range", "")
            if byte_range.startswith("bytes="):
                try:
                    bounds = byte_range[6:].split(",", 1)
                    if len(bounds) != 1:
                        raise ValueError
                    first, last = bounds[0].split("-", 1)
                    if first:
                        start = int(first)
                        end = int(last) if last else end
                    else:
                        suffix = int(last)
                        start = max(0, len(data) - suffix)
                    if start < 0 or start >= len(data) or end < start:
                        raise ValueError
                    end = min(end, len(data) - 1)
                    status = 206
                except ValueError:
                    self.send_response(416)
                    self.send_header("Content-Range", f"bytes */{len(data)}")
                    self.end_headers()
                    return
            payload = data[start:end + 1]
            self.send_response(status)
            self.send_header("Content-Type", "application/pdf")
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Accept-Ranges", "bytes")
            if status == 206:
                self.send_header("Content-Range", f"bytes {start}-{end}/{len(data)}")
            self.send_header("Content-Disposition", f'inline; filename="{path.name}"')
            self.send_header("Cache-Control", "no-store, max-age=0")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(payload)
            return
        if route.startswith("/api/source/"):
            rel = unquote(route.removeprefix("/api/source/"))
            allowed = {item["path"] for item in catalog()}
            if rel not in allowed:
                return self.send_error(404)
            data = (ROOT / rel).read_text(encoding="utf-8")
            return self.send_bytes(data.encode(), "text/plain; charset=utf-8")
        if route == "/" or route == "/index.html":
            return self.serve(WEB / "index.html", "text/html; charset=utf-8")
        if route in ("/styles.css", "/app.js"):
            kind = "text/css; charset=utf-8" if route.endswith("css") else "text/javascript; charset=utf-8"
            return self.serve(WEB / route.lstrip("/"), kind)
        self.send_error(404)

    def send_json(self, value):
        self.send_bytes(json.dumps(value).encode(), "application/json; charset=utf-8")

    def serve(self, path, content_type):
        if not path.is_file():
            return self.send_error(404)
        self.send_bytes(path.read_bytes(), content_type)

    def send_bytes(self, data, content_type):
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store, max-age=0")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *_):
        pass


if __name__ == "__main__":
    print("Python practice studio → http://127.0.0.1:8000")
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
