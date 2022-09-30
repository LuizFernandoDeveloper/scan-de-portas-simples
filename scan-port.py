import socket

portas = [21, 22, 23, 25, 80, 443, 3306]

for porta in portas:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.05)
    codigo = sock.connect_ex(("google.com", porta))
    if codigo == 0: 
        print("Porta:", porta, "| Status: Aberta (", codigo,")")

    else:
        print("Porta:", porta, "| Status: Fechada (", codigo,")")