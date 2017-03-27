#coding:utf-8 
import socket
SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096
def sendbuf():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	bufsize=s.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
	print(bufsize)
	s.setsockopt(socket.SOL_TCP,socket.TCP_NODELAY,1)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SEND_BUF_SIZE)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RECV_BUF_SIZE)
	bufsize=s.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
	print(bufsize)
if __name__=="__main__":
	sendbuf()