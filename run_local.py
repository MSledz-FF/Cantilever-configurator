#!/usr/bin/env python3
"""Serve the Composite Cantilever Designer locally and open it in a browser."""

from __future__ import annotations

import contextlib
import http.server
import os
from pathlib import Path
import socket
import socketserver
import threading
import webbrowser


APP_DIR = Path(__file__).resolve().parent
DEFAULT_PORT = 8765


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        pass


def find_available_port(start: int = DEFAULT_PORT) -> int:
    for port in range(start, start + 100):
        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            if sock.connect_ex(("127.0.0.1", port)) != 0:
                return port
    raise RuntimeError("No available local port found.")


def main() -> None:
    os.chdir(APP_DIR)
    port = find_available_port()
    url = f"http://127.0.0.1:{port}/"

    with socketserver.TCPServer(("127.0.0.1", port), QuietHandler) as server:
        threading.Timer(0.35, lambda: webbrowser.open(url)).start()
        print(f"Composite Cantilever Designer: {url}")
        print("Press Ctrl+C to stop.")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
