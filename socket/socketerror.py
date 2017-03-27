#coding:utf-8  
import sys
import socket
import argparse
def main():
	'''命令行传参'''
	parser = argparse.ArgumentParser(description="socket error examles")#命令行输入变量
	parser.add_argument('--host',action='store',dest='host',required=False)
	parser.add_argument('--port',action='store',dest='port',type=int,required=False)
	parser.add_argument("--file",action="store",dest='file',required=False)
	given_args=parser.parse_args()#接收变量
	host=given_args.host
	port=given_args.port
	filename=given_args.file
	'''套接字'''
	try:#创建套接字
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	except socket.error,e:
		print(e)
		sys.exit(1)
	'''连接'''
	try:#连接主机
		s.connect((host,port))
	except socket.gaierror,e:#主机不存在
		print(e)
		sys.exit(1)
	except socket.error,e:#端口无服务
		print(e)
		sys.exit(1)
	'''get 传参'''
	try:#发送文件
		s.sendall("GET %s HTTP/1.0 \r\n\r\n" % filename)
	except socket.error,e:
		print(e)
		sys.exit(1)

	while 1:
		'''缓冲区'''
	 	try:
	 		buf = s.recv(2048)#缓冲区
	 	except socket.error,e:
	 		print(e)
	 		exit(1)
	 	if not len(buf):
	 		break
	 	'''打印返回值'''
	 	sys.stdout.write(buf)

if __name__=="__main__":
	main()
