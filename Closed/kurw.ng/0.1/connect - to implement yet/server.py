import connect
from script import run
from script import parseFile

def server():
	Lnr = connect.createServer()
	sendable="True"
	while(sendable):
		sendable = connect.listen(Lnr, 30)
		run(parseFile(sendable),Lnr)
	shutdownListener(Lnr)
