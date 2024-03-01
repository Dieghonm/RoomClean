# server_interface.py
import tkinter as tk

class ServerInterface:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback
        # self.message = message

        self.root.title("Server Interface")

        self.messages_text = tk.Text(self.root)
        self.messages_text.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(padx=10, pady=5)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        # self.receive_thread = Thread(target=self.receive_messages)
        # self.receive_thread.start()

    def send_message(self):
        message = self.entry.get()
        self.messages_text.insert(tk.END, f"Server: {message}\n")
        self.callback(message)

    def receive_text(self, text):
        self.messages_text.insert(tk.END, f"Received message: {text}\n")
        self.callback('callback')
        print('interface')

    def start_interface(self):
        self.root.mainloop()



