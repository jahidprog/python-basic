"""A tiny, dependency-free browser for the Python practice repository."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse
import json
import re

ROOT = Path(__file__).resolve().parent
WEB = ROOT / "web"
GROUPS = {
    "basics": ("Foundations", "01"),
    "data-structures": ("Data structures", "02"),
    "functions": ("Functions", "03"),
    "oop": ("Object-oriented", "04"),
    "problems": ("Coding problems", "05"),
    "projects": ("Projects", "06"),
    "experiments": ("Experiments", "07"),
}


def catalog():
    items = []
    for category, (label, order) in GROUPS.items():
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
