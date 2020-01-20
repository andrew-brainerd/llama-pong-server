from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socketserver
import datetime
from urllib import parse

from pong_service import PongService

PORT = 45322

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        print(parsed_path)
        if self.path == '/time':
            self._do_time()
        elif self.path == '/users':
            PongService.test()

    def _do_time(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        current_time = str(datetime.datetime.now())
        message = json.dumps({ 'time': current_time })
        self.wfile.write(bytes(message, 'utf8'))

def run():
    print(f'Starting server at port {PORT}...')
    server_address = ('127.0.0.1', PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

run()