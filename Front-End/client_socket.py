import socket

class ClientSocket:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None

    def connect_to_server(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

    def send_message(self, message):
        self.client_socket.send(message.encode('utf-8'))

    def receive_message(self):
        return self.client_socket.recv(1024).decode('utf-8')

    def close_connection(self):
        self.client_socket.close()
