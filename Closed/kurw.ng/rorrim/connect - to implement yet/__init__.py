print "Loading the CONNECT package..."

from time import sleep
import socket

def createClient():
	ADDRESS = "127.0.0.1"
	#ADDRESS=socket.gethostname()
	PORT = 1488
	net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	net.setblocking(0)
	net.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	while(1):	
		try:
			net.connect((ADDRESS, PORT))
			break
		except socket.error:
			PORT += 1
	print "PORT: " + str(PORT)
	return net

def createServer(): #this actually creates a single connection, not a connection-creating Server func
	ADDRESS=socket.gethostname()
	PORT = 1488
	net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	net.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	net.bind(('', PORT))
	print "Port Estabilished"
	net.listen(5)
    	(clientsocket, address) = net.accept()
	print "Socket Created"
	return clientsocket

def shutdownListener(listener):
	try:
		net.shutdown(socket.SHUT_RDWR)
		net.close(socket.SHUT_RDWR)
	except:
		pass
	return True

def listen(listener, timeout=0):
	BUFFERSIZE,cnt=1024,0
	data = ""
	if(timeout): listener.settimeout(timeout)
	print "I AM LISTENING"
	try:
		data = listener.recv(BUFFERSIZE)
	except:
		return None
	if(data==""):
		shutdownListener(listener)
		return None
	if(data!=""): 
		return data
	return

def send(listener, message):
	try:
		listener.send(message)
	except:
		pass
	return

