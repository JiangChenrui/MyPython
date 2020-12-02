import socket
import sys


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8001))
    while True:
        data = input('Please input data:')
        if not data:
            break
        try:
            sock.sendall(data)
        except socket.error as e:
            print('Send Failed...', e)
            sys.exit(0)
        print('Send Successfully')

        res = sock.recv(4096)
        print(res)
    sock.close