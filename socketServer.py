# -*- coding:utf-8 -*-
import socket
import sys


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket Created')

    try:
        sock.bind(('127.0.0.1', 8001))
    except socket.error as e:
        print('Bind Failed...', e)
        sys.exit(0)
    
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        print(conn, addr)
        while True:
            data = conn.recv(4096)
            if not data:
                print("输入数据有误")
                break
            print('recive:', data.decode())
            conn.send(data.upper())
        conn.close()