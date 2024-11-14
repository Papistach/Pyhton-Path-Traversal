import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleRouter(BaseHTTPRequestHandler):
    def do_GET(self):
        path = f"./projets/webserver/www{self.path}"
        print(path)

        if os.path.exists(path):
            with open(path, "rb") as file:
                self.send_response(200)
                self.send_header("Content-Type", "text/html charset=utf-8")
                self.end_headers()
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/html charset=utf-8")
            self.end_headers()
            self.wfile.write(b"404")


server_adress = ("", 8080)
httpd = HTTPServer(server_adress, SimpleRouter)
print(f"Server launched on http://localhost:8080")
httpd.serve_forever()
