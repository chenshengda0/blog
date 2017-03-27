#coding:utf-8 
import socket
from binascii import hexlify
def ipv4():
	for ip in ['192.168.141.1','127.0.0.1']:
		ip_addr=socket.inet_aton(ip)#将字符串ip地址转换为32位的网络序列ip地址
		unpacked=socket.inet_ntoa(ip_addr)
		print(hexlify(ip_addr))

if __name__=="__main__":
	ipv4()