from socket import *
udp_socket = socket(AF_INET,SOCK_DGRAM)
addr = ('192.168.137.1',8080)
data = input('请输入要发送的数据：')
udp_socket.bind(('',8899))
udp_socket.sendto(data.encode('gb2312'),addr)
udp_rec = udp_socket.recvfrom(1024)
print("接收到来自%s的消息:'%s'"%(udp_rec[1],udp_rec[0].decode('gb2312')))
udp_socket.close()