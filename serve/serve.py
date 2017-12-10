import SimpleHTTPServer
import SocketServer
import io
import re

PORT = 5000
REGEX = r'\{\{[^\}]*\}\}'
REGEXCODE = r'\{\{[ ]*code[ ]*\}\}'

F1 = open("index.html", "r")
DATA = F1.read()
F1.close()
DATAEMPTY = re.sub(REGEX,'', DATA)

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(DATAEMPTY)
        return
    def do_POST(self):
        try:
            A = self.rfile.read(
                int(self.headers.getheader('content-length'))
            ).split("&")[0]

            assert  A[0:5] == "code="
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(re.sub(REGEXCODE,A[5:], DATA))
        except:
            return self.send_response(500)
        return

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()