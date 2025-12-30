from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Git project!")

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), SimpleHandler)
    print("Server running on http://localhost:8080")
    server.serve_forever()
