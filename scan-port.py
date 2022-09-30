import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect_ex(("google.com", 50))
sock.send("test\n".encode())

resposta = sock.recv(1024)

print(resposta)