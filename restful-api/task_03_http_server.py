#!/usr/bin/python3
"""Module that implements a simple API using http.server"""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Simple API handler class"""

    def do_GET(self):
        """Handles GET requests"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server = http.server.HTTPServer(('0.0.0.0', 8000), SimpleAPIHandler)
    server.serve_forever()
