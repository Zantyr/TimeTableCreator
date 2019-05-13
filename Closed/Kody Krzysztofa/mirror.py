slownikkontrolny = {}
#start
print ">ZALOGUJ SIE KURWO<"
log = raw_input()
if log != "kurwa":
	print ">BAD PASSWORD KURWO<"
	quit()
print ">WITAJ KURWO<"
print "Co chcialbys uczynic, ruchaczu foreva?"
slownikkontrolny["ruchaczforeva"] = False
slownikkontrolny["wojnaforeva"] = True
while(not slownikkontrolny["ruchaczforeva"]):
	command = raw_input()
	if command == "wyjdz":
		print ">Wychodzimy kurwa."
		quit()
	if command == "wojna":
		print ">Chyba Cie pojebalo. Ale jak chcesz. Zabieramy Cie na wojne!<"
		slownikkontrolny["ruchaczforeva"] = True
		slownikkontrolny["wojnaforeva"] = False
while(not slownikkontrolny["wojnaforeva"]):
	command = raw_input()
	if command == "wroc":
		print ">Wracamy do glownego menu kurwa.<"
		slownikkontrolny["ruchaczforeva"] = False
		slownikkontrolny["wojnaforeva"] = True
	if command == "wyjdz":
		print ">FRAJER DEZERTERUJE! ZAJEBAC KURIWA ZYDA W DUPE JEBANEGO PETRU!<"
		quit()
	if command == "zabic kurwa tych ludzi":
		print ">>>>>CONGRATULATIONZ<<<<<"
		print "You've just won the fucking game. gz scrub."
		quit()
