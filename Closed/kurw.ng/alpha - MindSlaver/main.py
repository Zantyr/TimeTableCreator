#This program is made to take partial control of the computer it is installed on. The clue is to make it a computational bot for your own purposes
#Of course to make it more useless and more educational all commands are implemented through a brand new interpreted scriptlang.
#Enjoy - MindSlaver - 2016, Zantyr

#clear console
from time import sleep
import os
os.system('cls' if os.name=='nt' else 'clear')

#import settings
from defs import *

#append modules
import connect
import db
import script

def Menu():
	global DEFAULTSCRIPT, ASKFORFILE, MODESELECT, DEFAULTMODE, doIWannaListen, doIWannaLocal
	if MODESELECT:
		while 1:
			q = raw_input("Wanna listen or command or local interpreter? (listen/command/local/none): ")
			if q=="listen": doIWannaListen = True
			elif q=="command": doIWannaLocal = False
			elif q=="local": doIWannaLocal = True
			else: continue
			break		
	else: doIWannaListen = DEFAULTMODE
	return

#main loop
def main():
	global DEFAULTSCRIPT, ASKFORFILE, MODESELECT, DEFAULTMODE, doIWannaListen, doIWannaLocal
	Menu()
	if doIWannaListen:
		script.server()	
	else:
		if ASKFORFILE: filename = raw_input("Gimme da filnaem, nigga: ")
		else: filename = DEFAULTSCRIPT
		if doIWannaLocal:
			script.functions["!zapytaj"] = script.localGet
			script.functions["!wyjeb"] = script.localOut
			with open(filename, "r") as fuck:
				sendable = fuck.read()
			script.run(script.parseFile(sendable))
		else:
			Lnr = connect.createClient()		
			with open(filename, "r") as fuck:
				sendable = fuck.read()
				connect.send(Lnr, sendable)
			print "\n\n>> File sent"
			while 1:
				data = connect.listen(Lnr)
				if(data == "CLOSE"):break
				if(data):script.localRun(Lnr,data)
				else: sleep(1)
			connect.shutdownListener(Lnr)
	return

#runs things
main()
