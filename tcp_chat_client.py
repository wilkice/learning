import socket

tcp_cilent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_cilent.connect(('192.168.70.109', 8888))

tcp_cilent.send("I'm client.".encode())
recvdata = tcp_cilent.recv(1024)
print(recvdata.decode())
tcp_cilent.close()