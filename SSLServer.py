import ssl
import socket


class SSLServer:

    def __init__(self):
        pass

    def deal_with_client(self, connstream):
        data = connstream.recv(1024)
        # empty data means the client is finished with us
        while data:
            print(data)
            data = connstream.recv(1024)
            # finished with client

    def setup(self):
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile="certs/server.crt", keyfile="certs/server.key")

        bindsocket = socket.socket()
        bindsocket.bind(('127.0.0.1', 12443))
        bindsocket.listen(5)

        while True:
            newsocket, fromaddr = bindsocket.accept()
            connstream = context.wrap_socket(newsocket, server_side=True)
            try:
                self.deal_with_client(connstream)
            finally:
                connstream.shutdown(socket.SHUT_RDWR)
                connstream.close()


if __name__ == '__main__':
    sslServer = SSLServer()
    sslServer.setup()