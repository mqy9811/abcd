
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = input("请输入传输数据：")
adrr = ('10.0.54.222', 8080)
print(adrr)
s.bind(('', 12345))
s.sendto(data.encode("gb2312"), adrr)
recv_meg = s.recvfrom(1024)
print(recv_meg)
print(recv_meg[1], recv_meg[0].decode("gb2312"))
s.close()
