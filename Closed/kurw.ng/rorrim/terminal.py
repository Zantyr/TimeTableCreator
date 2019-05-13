'''
TERMINAL:
	SERVER:
		CREATE SOCKET
		LISTEN FOR CONNECTIONS
		IF CONNECTION ACCEPTED CREATE LISTENER TERMINAL
	LISTENER:
		LISTEN TO THINGS
		INTERPRET THEM SENDING THE SOCKET TO RUN FUNCTION
		HAVE I/O FUNCTIONS
	CLIENT:
		CONNECT TO SOCKET
		SEND THINGS

TERMINAL:
	SERVER()
	LISTEN()
	CLIENT()
	__INIT__()
	CLOSE()
	PRINTSEND()
	PRINTRECV()
	

MODIFY THE RUN FUNCTION TO SEND THROUGH SOCKET
ENSURE PRINT AND RAW_INPUT IN LOOP

LISTEN LOOP():
	LISTEN FOR COMMANDS
	EVALUATE THE COMMAND
		WHEN PRINT:
		'''

import socket
import threading

#call __init__
#call listen thread
#listen thread creates a new subsocket-thread
#subsocket thread contains listening function
class Terminal:
	def interpret(self):
		while(1)
			pass
	def setCurrentTerminal(self, integer):
		pass
	def send(self, asc):
		if mode="server":
			pass #raise TerminalError
		if mode="monoclient":
			self.terminal.sendall(asc)
		if mode="polyclient":
			pass #STILL TO DO		
	def write(self, asc):
		if mode="server":
			self.clients[self.currentclient].sendall(asc)
		if mode="monoclient":
			self.terminal.sendall(asc)
		if mode="polyclient":
			pass #STILL TO DO
	def read(self, asc):
		if mode="server":
			self.clients[self.currentclient].sendall(asc)
		if mode="monoclient":
			self.terminal.sendall(asc)
		if mode="polyclient":
			pass #STILL TO DO
	def close(self):
		for i in self.clients:
			i.close()
			#terminate the threads of clients
		self.terminal.close()
	def listen(self):
		self.terminal.listen(2)
		(clientsocket, address) = self.terminal.accept()
		self.currentclient = len(self.clients)
		self.clients.append(clientsocket)
		self.clientthreads.append(threading.Thread(target=self.interpret))
		self.clientthreads[-1].run()
	def __init__(self, mode, ADDRESS='localhost', PORT=1488):
		self.terminal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.terminal.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.mode = mode
		if mode="server":
			self.terminal.bind(('', PORT))
			self.thread = threading.Thread(target=self.listen)
			self.clients = []
			self.thread.run()
		if mode="monoclient":
			self.terminal
			self.terminal.connect((ADDRESS, PORT))
		if mode="polyclient":
			pass #STILL TO DO

##IN FILE main##

os.system('cls' if os.name=='nt' else 'clear')
MainServer = Terminal("server")
MainClient = Terminal("monoclient")
MainClient.send("!run \"script.xD\"") #to implement
while(True):
	MainClient.send(raw_input("$: "))
MainServer.close()
MainClient.close()
