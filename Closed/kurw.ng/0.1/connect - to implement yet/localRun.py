import re
from connect import send
def localRun(conn,strIN):
	if(re.match("PROMPT (.*)",strIN)):
		send(conn,raw_input(re.match("PROMPT (.*)",strIN).group(1)))
	if(re.match("PRINT (.*)",strIN)):
		print re.match("PROMPT (.*)",strIN).group(1)
	if(re.match("FSEND ([^ ]*) #([0-9a-f]*)",strIN)):
		pass #to be written, saving function
	if(re.match("FGET ([^ ]*)",strIN)):
		pass #to be written, getting function
	return
