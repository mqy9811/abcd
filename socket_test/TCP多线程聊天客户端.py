import socket
import threading
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.bind(("", 8888))

client_socket.connect(("10.0.30.33", 9999))


def recv_message(client_socket):
    recv_meg = client_socket.recv(1024)
    print("8888收到：{}".format(recv_meg.decode("gb2312")))


def send_message(client_socket):
    send_addr = input("发送给（8989,9898）：")
    send_meg = input("发送：")
    send = [send_addr, send_meg]
    send_context = json.dumps(send)
    client_socket.send(send_context.encode("gb2312"))


while True:
    t_r = threading.Thread(target=recv_message, args=(client_socket,))
    t_s = threading.Thread(target=send_message, args=(client_socket,))

    t_r.start()
    t_s.start()
    t_r.join()
    t_s.join()

