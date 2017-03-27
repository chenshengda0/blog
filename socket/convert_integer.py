#coding:utf-8  
import socket
def convert_integer():
	'''网络字节序与主机字节序'''
	data=12345
	print(socket.ntohl(data))#32位
	print(socket.htonl(data))#32位
	print(socket.ntohs(data))#16位
	print(socket.htons(data))#16位

if __name__=="__main__":
	convert_integer()
