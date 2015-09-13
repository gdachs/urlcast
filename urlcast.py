#!/usr/bin/env python

#from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from subprocess import call
import urlparse

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        if parsed_path.path.endswith("urlcast"):
            self.send_response(200)
            self.send_header('Content-type',	'text/html')
            self.end_headers()
            url = parsed_path.query.split("=")[1]
            self.wfile.write("casted url: " + url)
            call(["google-chrome", url])

        return
                
def main():
    try:
        server = HTTPServer(('', 9999), MyHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()

