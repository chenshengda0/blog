#coding:utf-8 
import socket
def find_service_name():
	'''通过端口获取服务名，需知道协议名'''
	procotolname="tcp"
	for port in [25,80]:
		print(socket.getservbyport(port,procotolname))
	print(socket.getservbyport(53,'udp'))
if __name__=="__main__":
	find_service_name()
