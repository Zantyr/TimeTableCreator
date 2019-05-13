#CV

#introduction - build curiosity
#resume of personality
#skill presentation
#other interests
#person presentation and contact data
import socket
import re
import matplotlib.pyplot as pl
from math import sin
import os

def plotsin():
	x,y = [],[]
	for i in range(501):
		x.append(0.01*i)
	for i in x:
		y.append(sin(i))
	pl.plot(x,y)
	pl.show()
	return

def viewhome():
	ls = os.listdir("\\home")
	for i in ls:
		print ls
	return

def getMessage(toOpen):
	header = "HTTP/1.1\nContent-Type: text/html; charset=UTF-8\n\n"
	filename = "files"+os.sep+toOpen
	with open((filename),"r") as f:
		message = f.read()
	return header + message

def extract(string):
	try:
		mess = re.search("PLOT=Plot.21",string)
		if mess:
			plotsin()
	except:
		print "Nought"
		mess = ""
	try:
		mess = re.search("OS=View.21",string)
		if mess:
			viewhome()		
	except:
		print "Nought"
		mess = ""
	return

#MAIN HTML SERVER

PORT = 1488
BUFFERSIZE=1024
net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
net.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
net.bind(('', PORT))
while(1):
	print "Port Estabilished"
	net.listen(2)
	(clientsocket, address) = net.accept()
	print "Socket Created"
	data = clientsocket.recv(BUFFERSIZE)
	print data
	try:
		toOpen = re.search("(GET|POST) .(.*\.html)",data).group(2)
		print "FILE TO BE FOUND: " + toOpen
	except:
		print "Error Occured - no page found - returning HOME"
		toOpen = "index.html"
	extract(data)
	message = getMessage(toOpen)
	clientsocket.send(message)
	clientsocket.close()
	print "Page Sent"
net.shutdown(socket.SHUT_RDWR)
net.close(socket.SHUT_RDWR)
