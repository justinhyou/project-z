import time
import urllib.parse as urlparse

from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

from DataSupplier import DataSupplier
from DataTypeSource import DataTypeSource

HOST_NAME = 'localhost'
PORT_NUMBER = 9000


class DataServer(BaseHTTPRequestHandler):

    dataSupplier = DataSupplier()

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        paths = {
            '/info': {'status': 200}
        }

        if self.path in paths:
            self.respond(paths[self.path])
        else:
            self.respond({'status': 500})

    def handle_http(self, status_code, path):
        parsed = urlparse.urlparse(path)
        parsed_qs = parse_qs(parsed.query)
        print(parsed_qs)

        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        content = self.dataSupplier.getData(parsed_qs)
        return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['status'], self.path)
        self.wfile.write(response)

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), DataServer)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))