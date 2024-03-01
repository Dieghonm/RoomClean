import tkinter as tk
from server_socket import ServerSocket
from server_interface import ServerInterface

class Server:
    def __init__(self):
        self.root = tk.Tk()
        self.interface = ServerInterface(self.root, self.update_text)
        self.socket = ServerSocket()
        self.socket.start_server()
        self.client_socket = None
        self.receive_messages('texto do server para a interface')
        self.root.mainloop()

    def update_text(self, text):
        print("Received text from child:", text)

    def receive_messages(self, text):
        print('seilah2', text)
        self.interface.receive_text(text)
        # while True:
        #     self.client_socket = self.socket.accept_connection()
        #     message = self.socket.receive_message(self.client_socket)
        #     if message.lower() == 'quit':
        #         break
        #     self.interface.receive_text(message)
        #     self.socket.send_message(self.client_socket, "Message received")
        #     self.socket.close_connection(self.client_socket)

if __name__ == "__main__":
    server = Server()