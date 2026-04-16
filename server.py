#!/usr/bin/env python3
"""
Rappod Stationery - Static Dev Server
Run: python server.py
Opens: http://localhost:8080
"""
import http.server, socketserver, webbrowser, os, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()
    def log_message(self, fmt, *args):
        print(f"  {args[0]} {args[1]}")

with socketserver.TCPServer(("", PORT), Handler) as s:
    url = f"http://localhost:{PORT}"
    print(f"\n  Rappod → {url}\n  Ctrl+C to stop\n")
    webbrowser.open(url)
    try: s.serve_forever()
    except KeyboardInterrupt: print("\n  Stopped.")
