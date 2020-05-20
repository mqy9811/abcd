
import socket

socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp.bind(("", 8899))
socket_tcp.listen(5)
clientSocket, clientInfo = socket_tcp.accept()
recv_meg = clientSocket.recv(1024)
print(clientInfo, recv_meg.decode("gb2312"))
clientSocket.close()
socket_tcp.close()
