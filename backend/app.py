import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("Hello from Effective Mobile!".encode("utf-8"))
        elif self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))
        else:
            self.send_error(404)


def get_port():
    port = os.getenv("PORT")
    if port is None:
        sys.exit("Error: PORT environment variable is not set.")
    return int(port)


port = get_port()
server = HTTPServer(("0.0.0.0", port), SimpleHandler)
print(f"Server running on http://localhost:{port}")
server.serve_forever()
