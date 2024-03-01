import socket
def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        
        return ip_address
    except socket.error as e:
        print(f"Erro ao obter o endereço IP: {e}")