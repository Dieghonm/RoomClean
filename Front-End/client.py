import threading
import tkinter as tk
from client_socket import ClientSocket
from client_interface import ClientInterface

def main():
    host = '127.0.0.1'  # Altere para o endereço IP do servidor
    port = 12345  # Altere para a porta em que o servidor está ouvindo

    # Criar o socket do cliente e conectar-se ao servidor
    client_socket = ClientSocket(host, port)
    client_socket.connect_to_server()

    # Criar a interface do cliente
    root = tk.Tk()
    app = ClientInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
