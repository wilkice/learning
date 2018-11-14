import socket, threading, os

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(('192.168.70.70', 6671))
file_name = input('pls input the file name with add and extension: ')
if os.path.exists(file_name):
    print('file is found. We will upload it asap')
    file_bytes = os.path.getsize(file_name)
    num_of_thread = file_bytes // 8
else:
    print('file can be found! Pls check the path. ')


def mutl_upload_threading(i):
    with open(file_name, 'rb') as f:
        if i == 8:
            f.seek(7*num_of_thread)
            partdata = f.read()
            tcp_socket.send(partdata)
        else:
            f.seek(num_of_thread*i)
            partdata = f.read(num_of_thread)
            tcp_socket.send(partdata)


for num_of_threading in range(1,9):

    mythreading = threading.Thread(target=mutl_upload_threading, args=(num_of_threading,))
    mythreading.start()
    print('threading', str(num_of_threading), 'is running! ')









