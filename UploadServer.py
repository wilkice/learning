''' 文件上传服务器'''

# 模块导入
# import socket

import socket
import threading
import os

# 封装上传类
class UploadServer(object):
    def __init__(self):
        # 建立socket连接
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 复用端口
        self.__server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定ip和端口
        self.__server_socket.bind(('', 7777))
        # 设置监听
        self.__server_socket.listen(128)
        # 定义拼接上传文件的序号
        self.__file_number = 0
        # # 上传文件的路径
        self.__path = "/Users/hto/Desktop/coo/"
        # 判断上传路径是否存在
        if not os.path.exists(self.__path):
            # 如果文件路径不存在 则创建
            os.mkdir(self.__path)

    # 处理客户端请求的方法
    def __handle_upload(self, client_socket, client_addr):
        # 将文件编号 + 1
        self.__file_number += 1
        # 接收文件 拼接文件名 以客户端的ip和来组合成文件名
        file_name = '%s-%d' % (client_addr[0], self.__file_number)

        # 写文件
        with open(self.__path + file_name, "wb") as f:
            # 循环接收数据
            while True:
                # 读上传数据
                file_data = client_socket.recv(1024)
                if file_data:
                    f.write(file_data)
                else:
                    break
        client_socket.close()


    # 启动上传服务
    def run(self):
        # 接收客户端请求
        client_socket, client_addr = self.__server_socket.accept()
        # 创建线程处理请求
        t = threading.Thread(target=self.__handle_upload, args=(client_socket, client_addr,))
        # 启动线程
        t.start()
        t.join()

    def close(self):
        self.__server_socket.close()



def main():
    # 启动文件上传服务器
    up_server = UploadServer()
    up_server.run()
    up_server.close()

if __name__ == '__main__':
    main()

