from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

LOGGER_URL = "http://logger:5000/log"

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        message = "Hello from Git project!"
        self.wfile.write(message.encode())

        try:
            requests.post(LOGGER_URL, data={"log": message})
        except Exception as e:
            print(f"Logger unavailable: {e}")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), SimpleHandler)
    print("Server running on http://0.0.0.0:8080")
    server.serve_forever()
