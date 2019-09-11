from socket import socket,AF_INET,SOCK_DGRAM
udp_socket = socket(AF_INET,SOCK_DGRAM)
addr = ('192.168.137.1',8080)
data = input('请输入要发送的信息：')
udp_socket.sendto(data.encode('gb2312'),addr)
udp_socket.close()