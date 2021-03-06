from script import functions
from script import howManyArgs
from script import IOsets
from connect import send

def get(*args):
	send(IOsets["listener"], "PROMPT "+str(args[0]))
	return #listen(IOsets["listener"])

def localGet(*args):
	return raw_input(str(args[0]))

def create(*args):
	return []

def addone(*args):
	args[0].append(args[1])
	return None

def edit(*args):
	args[0][int(args[1])] = args[2]
	return None

def delete(*args):
	args[0] = args[0][:int(args[1])]+(args[0][int(args[1])+1:] if int(args[1])<(len(args[0])-1) else [])
	return None

def elem(*args):
	return args[1][int(args[0])]

def out(*args):
	send(IOsets["listener"], "PRINT "+str(args[0]))
	return None

def localOut(*args):
	print(str(args[0]))
	return


def lenOfKurwa(*args):
	return len(args[0])

functions["!zapytaj"] = get
functions["!wyjeb"] = out
functions["!kurwa"] = create
functions["!dojeb"] = addone
functions["!zmien"] = edit
functions["!wypierdol"] = delete
functions["!grubosc"] = lenOfKurwa
functions["!pierdolnik"] = elem
howManyArgs["!zapytaj"] = 1
howManyArgs["!wyjeb"] = 1
howManyArgs["!kurwa"] = 0
howManyArgs["!dojeb"] = 2
howManyArgs["!zmien"] = 3
howManyArgs["!wypierdol"] = 2
howManyArgs["!grubosc"] = 1
howManyArgs["!pierdolnik"] = 2
