import tkinter as tk

class ClientInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Interface")

        self.messages_text = tk.Text(self.root)
        self.messages_text.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(padx=10, pady=5)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

    def send_message(self):
        message = self.entry.get()
        self.messages_text.insert(tk.END, f"Sent message: {message}\n")
        # Aqui você pode chamar uma função para enviar a mensagem para o servidor
