#coding:utf-8 
import socket
def test_socket_timeout():
	"""设置与获取套接字超时时间"""
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#第一个参数为地址族，第二个参数为套接字类型
	print(s.gettimeout())
	s.settimeout(100)#设置超时时间
	print(s.gettimeout())
if __name__ == "__main__":
	test_socket_timeout()