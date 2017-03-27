#coding:utf-8
import socket
def gethost():
	host = socket.gethostname()
	try:
		ip = socket.gethostbyname(host)
	except socket.error,errmsg:
		ip = errmsg
	print(ip)
if __name__=="__main__":
	gethost()

