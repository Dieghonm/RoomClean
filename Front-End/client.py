import tkinter as tk
import socket
from threading import Thread

class ClientInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Interface")

        # Frame para conter os campos de entrada do IP, porta e nome de usuário
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(padx=10, pady=5)

        # Campo de entrada para o nome de usuário
        self.username_label = tk.Label(self.input_frame, text="Username:")
        self.username_label.pack(side=tk.LEFT)
        self.username_entry = tk.Entry(self.input_frame, width=15)
        self.username_entry.pack(side=tk.LEFT)

        # Campo de entrada para o endereço IP
        self.ip_label = tk.Label(self.input_frame, text="IP:")
        self.ip_label.pack(side=tk.LEFT)
        self.ip_entry = tk.Entry(self.input_frame, width=15)
        self.ip_entry.pack(side=tk.LEFT)
        self.ip_entry.insert(tk.END, "127.0.0.1")  # Sugestão de preenchimento com o endereço IP loopback padrão

        # Campo de entrada para a porta
        self.port_label = tk.Label(self.input_frame, text="Port:")
        self.port_label.pack(side=tk.LEFT)
        self.port_entry = tk.Entry(self.input_frame, width=10)
        self.port_entry.pack(side=tk.LEFT)
        self.port_entry.insert(tk.END, "12345")  # Sugestão de preenchimento com a porta padrão

        self.connect_button = tk.Button(root, text="Connect", command=self.connect_to_server)
        self.connect_button.pack(pady=5)

        self.messages_text = tk.Text(root)
        self.messages_text.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(padx=10, pady=5)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        self.client_socket = None

    def connect_to_server(self):
        username = self.username_entry.get().upper()
        ip = self.ip_entry.get()
        port = int(self.port_entry.get())
        
        # Exibir os valores do IP e da porta como mostradores de texto
        self.username_label.config(text=f"IP: {username}")
        self.username_entry.pack_forget()
        self.ip_label.config(text=f"IP: {ip}")
        self.ip_entry.pack_forget()
        self.port_label.config(text=f"Port: {port}")
        self.port_entry.pack_forget()
        
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((ip, port))
            self.receive_thread = Thread(target=self.receive_messages)
            self.receive_thread.start()
            self.messages_text.insert(tk.END, "Connected to server\n")
        except Exception as e:
            self.messages_text.insert(tk.END, f"Error connecting to server: {e}\n")

    def send_message(self):
        if self.client_socket:
            username = self.username_entry.get().upper()
            message = self.entry.get()
            full_message = f"{username}: {message}"
            self.client_socket.send(full_message.encode('utf-8'))
            self.entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                self.messages_text.insert(tk.END, f"{data.decode('utf-8')}\n")
            except ConnectionAbortedError:
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = ClientInterface(root)
    root.mainloop()
