import socket, threading
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(('192.168.67.94',6666))
print('connected with server')

def send():
    while True:
        send = input('pls input something: ')
        tcp_socket.send(send.encode('gbk'))


def reve():
    while True:
        text = tcp_socket.recv(1024)
        print('rece:',text.decode('gbk'))


if __name__ == '__main__':
    sub_send = threading.Thread(target=send)
    sub_reve = threading.Thread(target=reve)
    sub_send.start()
    sub_reve.start()



