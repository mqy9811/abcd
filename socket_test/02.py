import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 12345))
addr = ('10.0.219.189', 8080)


def send():
    while True:
        data = input("<<")
        s.sendto(data.encode("gb2312"), addr)


def recv():
    while True:
        recv_mesg = s.recvfrom(1024)
        print(">>", recv_mesg[0].decode("gb2312"))


if __name__ == "__main__":
    send = threading.Thread(target=send)

    recv = threading.Thread(target=recv)
    send.start()
    recv.start()
    send.join()
    recv.join()