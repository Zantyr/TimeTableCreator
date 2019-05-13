import re
try:
	import matplotlib.pyplot as pl
	PLOTTABLE = True
except ImportError:
	print "Cannot import matplotlib"
	PLOTTABLE = False

functions,howManyArgs={},{}

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

functions["+"]=add
functions["-"]=sub
functions["*"]=mul
functions["/"]=div
functions["^"]=power
howManyArgs["+"]=2
howManyArgs["-"]=2
howManyArgs["*"]=2
howManyArgs["/"]=2
howManyArgs["^"]=2

def whatType(arg):
	try:
		x = 2.0  + arg
		return "numeric"
	except TypeError:
		try:
			if(arg=="x"): return "identifier"
			else: return None
		except TypeError:
			if(isList(arg)): return "list"
			else: return None

def assoc(i):
	left=["+","-","*","/"]
	if i in left: return True
	else: return False

def precedence(i,j):
	pre = {}
	pre["("]=-4
	pre["+"]=1
	pre["-"]=1
	pre["*"]=2
	pre["/"]=2
	pre["^"]=3
	pre[")"]=99
	if((pre[i]<=pre[j] and assoc(i)) or (pre[i]<pre[j] and assoc(i))): return True
	else: return False

def upgradedSplit(strin):
	ret = strin.split(" ")
	return ret

def shuntingYard(strin):
	operator = "(\+|-|\*|\/|(\^)|sin|cos|tan|tg|cotan|ctg|ln|exp)"
	numeric = "-?(\d+(\.\d*)?)"
	identifier = "(x)"
	left = "\("
	right = "\)"
	output = []
	stack = []
	tokens = upgradedSplit(strin)
	for token in tokens:
		x = re.match(numeric,token)
		if(x): 
			output.append(float(x.group(1)))
			continue
		x = re.match(identifier,token)		
		if(x): output.append(x.group(1))
		x = re.match(operator,token)
		if(x):
			op = x.group(1)
			while(len(stack)):
				temp = stack.pop()
				if(precedence(op,temp)):output.append(temp)
				else:
					stack.append(temp)				
					break
			stack.append(op)
		x = re.match(left,token)
		if(x): stack.append("(")
		x = re.match(right,token)
		if(x):
			while(len(stack)):
				temp = stack.pop()
				if(temp=="("):
					stack.append(temp)
					if(len(stack)):
						temp = stack.pop()
						if re.match(function,temp): output.append(temp)
					break
				else:
					output.append(temp)
	while(len(stack)):
		temp = stack.pop()
		if all((temp!="(",temp!=")")): output.append(temp)
		else: return False
	return output

def evaluate(strinput, val=0):
	operator = "(\+|-|\*|\/|(\^)|sin|cos|tan|tg|cotan|ctg|ln)"
	numeric = "-?(\d+(\.\d*)?)"
	identifier = "(x)"
	stack = []
	postfix = shuntingYard(strinput)
	for i in postfix:
		#print stack
		if whatType(i)=="numeric":stack.append(i)
		if whatType(i)=="identifier": stack.append(val)
		try:
			if re.match(operator,str(i)):
				args=[]
				for j in range(howManyArgs[i]):
					args = [stack.pop()] + args
				stack.append(functions[i](*args))
		except TypeError:
			print "KURWA BUONT TYPU"
	if(len(stack)>1):return None
	return stack[0]

def plotfun(asc,scale=10):
	x,y = [],[]
	for i in range(200):
		print i
		x.append((scale/100.0)*i-scale)
		y.append(evaluate(asc,(scale/100.0)*i-scale))
	print x,y
	pl.plot(x,y)
	pl.show()

#example
calcul = raw_input("Wyrazenie do obliczenia: ")
print evaluate(calcul)
fun = raw_input("y = ... :")
plotfun(fun,10)

