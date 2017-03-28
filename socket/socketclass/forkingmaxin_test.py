#coding:utf-8 
import os
import socket
import threading
import SocketServer
SERVER_HOST="localhost"
SERVER_PORT=0
BUF_SIZE=1024
ECHO_MSG="Hello echo server!"
class ForkingClient():#客户端
	"""客户端"""
	def __init__(self,ip,port):
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sock.connect((ip,port))

	def run(self):
		current_process_id=os.getpid()
		print("PID %s Sending echo message to the server : '%s' " %(current_process_id,ECHO_MSG))
		sent_data_length=self.sock.send(ECHO_MSG)
		print("Send : %d characters,so far..." % sent_data_length)
		response = self.sock.recv(BUF_SIZE)
		print("PID %s received : %s" %(current_process_id,response[5:]))

	def shutdown(self):
		self.sock.close()

class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):
	#SocketServer.BaseRequestHandler.__init__() 自动调用handle()方法
	def handle(self):
		data=self.request.recv(BUF_SIZE)
		current_process_id=os.getpid()
		response='%s: %s' %(current_process_id, data) #拼接字符串
		#print(response) 
		print("Server sending response [current_process_id : data]= [%s]" %response)
		self.request.send(response)
		return

class ForkingServer(SocketServer.ForkingMixIn,SocketServer.TCPServer,):
	pass

def main():
	server=ForkingServer((SERVER_HOST,SERVER_PORT),ForkingServerRequestHandler)
	ip,port=server.server_address
	server_thread=threading.Thread(target=server.serve_forever)
	server_thread.setDaemon(True)
	server_thread.start()
	print("Server loop running PID : %s" % os.getpid())
	client1=ForkingClient(ip,port)
	client1.run()
	client2=ForkingClient(ip,port)
	client2.run()
	server.shutdown()
	client1.shutdown()
	client2.shutdown()
	server.socket.close()

if __name__=="__main__":
	main()

###文件在windows执行AttrbuteError:'module' object has no attrbute 'fork'，linux执行正常
###主线程中创建一个ForkingServer实例，作为守护进程在后台运行，然后创建两个客户端交互
