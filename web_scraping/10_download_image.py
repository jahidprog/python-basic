"""Exercise 10: Download an image from a direct image URL.

Replace IMAGE_URL with a direct image URL you have permission to download.
"""
from pathlib import Path
import requests

IMAGE_URL = "https://httpbin.org/image/png"
output_path = Path("downloaded_image.png")

try:
    with requests.get(IMAGE_URL, stream=True, timeout=20) as response:
        response.raise_for_status()
        content_type = response.headers.get("content-type", "")
        if not content_type.startswith("image/"):
            raise ValueError(f"URL did not return an image (content-type: {content_type})")

        with output_path.open("wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
    print("Saved:", output_path.resolve())
except (requests.RequestException, OSError, ValueError) as exc:
    print("Download failed:", exc)
