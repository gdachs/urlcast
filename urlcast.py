#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from subprocess import Popen
import urlparse
import socket

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        if parsed_path.path.endswith("urlcast"):
            self.send_response(200)
            self.send_header('Content-type',	'text/html')
            self.end_headers()
            url = parsed_path.query.split("=", 1)[1]
            Popen(["google-chrome", "--start-fullscreen", url])
            self.wfile.write("casted url: " + url)
	else:
            self.send_response(200)
            self.send_header('Content-type',	'text/html')
            self.end_headers()
            self.wfile.write("Add this bookmarklet to your favourites: ")
            self.wfile.write("<a href=\"javascript:location.href='http://" +
                socket.getfqdn() + 
                ":9999/urlcast?url='+location.href\">Cast to TV</a>")
            self.wfile.write("<p>")
            self.wfile.write("Click on it to cast the current page to the TV")
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

