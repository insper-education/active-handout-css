#!/usr/bin/env python3
import http.server
import socketserver

PORT = 8090

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving CSS at: http://localhost:{PORT}")
    httpd.serve_forever()
