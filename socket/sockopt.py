#coding:utf-8 
import socket
import sys
def sockopt():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	old_state=s.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
	print(old_state)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	new_state=s.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
	print(new_state)
	local_port=8282
	srv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#套接字重用设置为1时,同时使用同一个端口可以连接上
	#设置为0时，一个端口只能连接一次，其余报错
	srv.bind(('',local_port))
	srv.listen(1)
	print(local_port)
	while True:
		try:
			connection,addr=srv.accept()
			print("connect by %s:%s" % (addr[0],addr[1]))
		except KeyboardInterrupt:
			break
		except socket.error,e:
			print(e)

if __name__=="__main__":
	sockopt()