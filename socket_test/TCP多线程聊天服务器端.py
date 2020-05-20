import socket
import threading
import json
"""
    TCP多线程聊天的服务器
"""
sockets = []

# 创建
sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定
sever_socket.bind(("", 9999))


def solve_meg(client_socket):
    # 客户端的信息
    j_message = client_socket.recv(1024)
    json_message = j_message.decode("gb2312")
    message = json.loads(json_message)

    # 重新发送
    for sender in sockets:
        sender.send(message[1].encode("gb2312"))


while True:
    # 监听
    sever_socket.listen()
    # 获取客户端发送的信息、客户端的信息
    client_socket, client_info = sever_socket.accept()
    print(client_socket)
    print("client_info:{}".format(client_info))
    sockets.append(client_socket)
    t = threading.Thread(target=solve_meg, args=(client_socket,))
    t.start()



