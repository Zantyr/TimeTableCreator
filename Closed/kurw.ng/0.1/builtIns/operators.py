from defs import functions
from defs import howManyArgs

def add(*args):
	try:
		return args[0]+args[1]
	except TypeError:
		print args[0],args[1],"BUONT TYPU"

def sub(*args):
	try:
		return args[0]-args[1]
	except TypeError:
		print args[0],args[1],"BUONT TYPU"

def mul(*args):
	try:
		return args[0]*args[1]
	except TypeError:
		print args[0],args[1],"BUONT TYPU"

def div(*args):
	try:
		return args[0]/args[1]
	except TypeError:
		print args[0],args[1],"BUONT TYPU"

def power(*args):
	try:
		return pow(args[0],args[1])
	except TypeError:
		print args[0],args[1],"BUONT TYPU"

def more(*args):
	try:
		if(args[0]>args[1]): return 1
		else: return 0
	except TypeError:
		return None

def less(*args):
	try:
		if(args[0]<args[1]): return 1
		else: return 0
	except TypeError:
		return None

def equals(*args):
	try:
		if(args[0]==args[1]): return 1
		else: return 0
	except TypeError:
		return None

def nomo(*args):
	try:
		if(args[0]>args[1]): return 0
		else: return 1
	except TypeError:
		return None

def noless(*args):
	try:
		if(args[0]<args[1]): return 0
		else: return 1
	except TypeError:
		return None

def notEquals(*args):
	try:
		if(args[0]==args[1]): return 0
		else: return 1
	except TypeError:
		return None

functions["+"]=add
functions["-"]=sub
functions["*"]=mul
functions["/"]=div
functions["^"]=power
functions[">>"]=more
functions["<<"]=less
functions["=="]=equals
functions[">="]=noless
functions["<="]=nomo
functions["!="]=notEquals
howManyArgs["+"]=2
howManyArgs["-"]=2
howManyArgs["*"]=2
howManyArgs["/"]=2
howManyArgs["^"]=2
howManyArgs[">>"]=2
howManyArgs["<<"]=2
howManyArgs["=="]=2
howManyArgs[">="]=2
howManyArgs["<="]=2
howManyArgs["!="]=2
