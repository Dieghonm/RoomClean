import socket
import tkinter as tk
from threading import Thread
from get_ip import get_ip_address

class ServerInterface:
    def __init__(self, root):
        self.root = root
        self.port = 12345
        self.root.title(f"Server ip:{get_ip_address()} / port:{self.port}\n")

        self.messages_text = tk.Text(root)
        self.messages_text.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(padx=10, pady=5)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', self.port))
        self.server_socket.listen(5)  # Permitindo até 5 conexões pendentes

        self.clients = []

        self.accept_thread = Thread(target=self.accept_clients)
        self.accept_thread.start()

    def accept_clients(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connected to {client_address}")
            self.clients.append((client_socket, client_address))
            receive_thread = Thread(target=self.receive_messages, args=(client_socket,))
            receive_thread.start()

    def send_message(self):
        message = self.entry.get()
        for client_socket, _ in self.clients:
            client_socket.send(message.encode('utf-8'))
        self.messages_text.insert(tk.END, f"Server: {message}\n")
        self.entry.delete(0, tk.END)

    def receive_messages(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                self.messages_text.insert(tk.END, f"Client: {data}\n")
                message = data
                for client_socket, _ in self.clients:
                    client_socket.send(message.encode('utf-8'))
            except ConnectionAbortedError:
                break



def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        
        return ip_address
    except socket.error as e:
        print(f"Erro ao obter o endereço IP: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ServerInterface(root)
    root.mainloop()