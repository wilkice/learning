
import  socket


class UploadClient(object):
    def __init__(self):
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        # 连接服务器
        self.__client_socket.connect(('', 7777))

    # 上传文件的方法
    def upload_file(self, file_path):
        with open(file_path, 'rb') as f:
            # 读取文件内容
            file_data = f.read(1024)
            while file_data:
                self.__client_socket.send(file_data)
                # 继续读取新数据
                file_data = f.read(1024)

    def close(self):
        self.__client_socket.close()

def main():
    up = UploadClient()
    # 上传文件
    up.upload_file('/Users/hto/Desktop/mycode/1.txt')
    up.close()


if __name__ == '__main__':
    main()

