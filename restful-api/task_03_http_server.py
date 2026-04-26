import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self._respond(200, "text/plain", "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._respond(200, "application/json", json.dumps(data))
        elif self.path == "/status":
            self._respond(200, "text/plain", "OK")
        elif self.path == "/info":
            data = {"version": "1.0", "description": "A simple API built with http.server"}
            self._respond(200, "application/json", json.dumps(data))
        else:
            self._respond(404, "text/plain", "Endpoint not found")

    def _respond(self, status, content_type, body):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), SimpleAPIHandler)
    print("Server running on port 8000...")
    server.serve_forever()
