#coding:utf-8 
import socket
import sys
import argparse
host = 'localhost'
def echo_client(port):
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_address=(host,port)
	sock.connect(server_address)
	try:
		message="Test message.This will be echoed"
		print("sending %s" % message)
		sock.sendall(message)
		amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_expected:
			data =sock.recv(16)
			amount_received += len(data)
			print("Received: %s" % data)
	except socket.errno,e:
		print("socket error: %s" % str(e))
	except Exception,e:
		print("Other Exception: %s" % str(e))
	finally:
		print("Closing connection to the server")
		sock.close()

if __name__=="__main__":
	parser=argparse.ArgumentParser(description="Socket server Example")
	parser.add_argument('--port',action='store',dest='port',type=int,required=True)
	given_args=parser.parse_args()
	port=given_args.port
	echo_client(port)		