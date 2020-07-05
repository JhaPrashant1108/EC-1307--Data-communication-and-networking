import socket
import http.client
import os.path
import json

class TCPServer : 
    def __init__(self, host='127.0.0.1', port=3000) :
        self.host=host
        self.port=port

    def handleRequest(self, data) :
        return data
        
    def start(self) : 
        #a new socket object
        sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #binding the address and port to the socket
        sckt.bind((self.host, self.port))

        #listening to session
        sckt.listen(5)

        print("Listening to ", sckt.getsockname())

        while True :
            #accepting the request from client
            conn, address = sckt.accept()
            print("Connected to", address)

            #getting data from request
            req = conn.recv(1024).decode()

            #preparing response to be sent
            res = self.handleRequest(req)

            #sending response
            conn.sendall(res.encode())

            #closing connection
            conn.close()

class HTTPServer(TCPServer):
    status_codes = http.client.responses

    headers = {
        'Server' : 'My Server',                 #Name of the server
        'Content-Type' : 'application/json'     #response will be a JSON object
    }

    def handleRequest(self, data):
        req = HTTPRequest(data)
        try :
            handler = getattr(self, "handle_{0}".format(req.method))
        except AttributeError :
            handler = self.handle_501
        return handler(req)

    def handle_GET(self, req) : 
        file = "JSON_data"+req.uri

        if(req.uri != "/" and os.path.exists(file)) :
            res_line = self.getResLine(200)
            res_header = self.getHeaders()

            with open(file) as f:
                res_body = f.read()
        else:
            res_line = self.getResLine(404)
            res_header = self.getHeaders()
            res_body = '{"error" : "404 Not Found"}'

        line_break = "\r\n"

        return "{0}{1}{2}{3}".format(
                res_line, 
                res_header, 
                line_break, 
                res_body
            )

    def handle_501(self, req) :
        res_line = self.getResLine(status_code=501)
        res_header = self.getHeaders()
        line_break = '\r\n'
        res_body = '{"error" : "501 Not Implemented"}'
        return "{0}{1}{2}{3}".format(
            res_line, res_header, line_break, res_body
        )

    def getHeaders(self, extra_headers = None) :
        header_copy = self.headers.copy() #copying the headers
            
        if extra_headers :
            header_copy.update(extra_headers)
            
        header_result = ""

        for h in self.headers : 
            header_result += "%s: %s\r\n" % (h, self.headers[h])
            
        return header_result
        

    def getResLine(self, status_code) : 
        return "HTTP/1.1 ""{0} {1}""\r\n".format(status_code, self.status_codes[status_code])

class HTTPRequest : 
    def __init__(self, data) : 
        self.uri = None
        self.method = None
        self.http_version = '1.1'
        self.headers = {}

        self.parse(data)
    
    def parse(self, data) :
        lines = data.split("\r\n")
        req_line = lines[0].split(' ')
        self.method = req_line[0]
        self.uri = req_line[1]                       
        if len(req_line) > 2 :
            self.http_version = req_line[2]
         

if __name__ == '__main__' :
    server = HTTPServer()
    server.start()