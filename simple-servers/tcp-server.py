# https://docs.python.org/3/library/socketserver.html

import socketserver

class MyTCPHandler(socketserver.StreamRequestHandler):

  def handle(self):
    # self.request is the TCP socket connected to the client
    self.data = self.rfile.readline().strip()
    print("{} wrote:".format(self.client_address[0]))
    print(self.data)
    # just send back the same data, but upper-cased
    self.request.sendall(self.data.upper())


if __name__ == "__main__":
  HOST, PORT = "localhost", 9999

  with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
    print("Starting server on", HOST, PORT)
    server.serve_forever()
