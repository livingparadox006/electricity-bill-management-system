import http.server
import socketserver
import os
import webbrowser

PORT = 8080
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

os.chdir(DIR)
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = "http://localhost:%d" % PORT
    print("Electricity Bill Management System Simulator")
    print("Serving at %s" % url)
    print("Press Ctrl+C to stop.")
    try:
        webbrowser.open(url)
    except Exception:
        pass
    httpd.serve_forever()
