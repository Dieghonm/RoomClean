import socket

class ServerSocket:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host = host
        self.port = port
        self.server_socket = None

    def start_server(self):
        print('socket')
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(10)
        print(f"Server listening on {self.host}:{self.port}")

    def accept_connection(self):
        client_socket, client_address = self.server_socket.accept()
        print(f"Connection established with {client_address}")
        return client_socket

    def receive_message(self, client_socket):
        message = client_socket.recv(1024).decode("utf-8")
        print(f"Received message: {message}")
        return message

    def send_message(self, client_socket, message):
        client_socket.send(message.encode("utf-8"))
        print("Message sent")

    def close_connection(self, client_socket):
        client_socket.close()
        print("Connection closed")
