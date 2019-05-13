from script import functions
from script import howManyArgs
from script import variables
from script import operator
from script import numeric
from script import identifier
from script import function
from script import separator
from script import string
from script import modifier
import re

def whatType(arg):
	global string, function, identifier,modifier
	try:
		x = 2.0  + arg
		return "numeric"
	except TypeError:
		try:
			if(re.match(string,arg)): return "string"
			elif(re.match(identifier,arg)): return "identifier"
			elif(re.match(function,arg)): return "function"
			elif(re.match(modifier,arg)): return "modifier"						
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
	pre[">>"]=-1
	pre["<<"]=-1
	pre["=="]=-1
	pre[">="]=-1
	pre["<="]=-1
	pre["!="]=-1
	if((pre[i]<=pre[j] and assoc(i)) or (pre[i]<pre[j] and assoc(i))): return True
	else: return False

def upgradedSplit(strin):
	ID = 0
	replace = []
	while(re.search(string,strin)):
		s = re.search("(.*)(\"[^\"\n]*\")(.*)",strin)
		strin = s.group(1)+"!&@"+str(ID)+s.group(3)
		replace.append(s.group(2))
		ID+=1
	ret = strin.split(" ")
	for i in range(ID):
		for n,el in enumerate(ret):
			if el=="!&@"+str(i):
				ret[n] = replace[i]
	return ret

def shuntingYard(strin):
	global operator, numeric, function, identifier, separator, string
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
		x = re.match(string,token)
		if(x): 
			output.append(x.string)		
			continue
		x = re.match(identifier,token)		
		if(x): output.append(x.group(1))
		x = re.match(function,token)
		if(x): stack.append(x.group(1))
		x = re.match(separator,token)
		if(x):
			temp = ""
			while(temp!="("):
				try:
					temp = stack.pop()
					if(temp=="("): stack.append(temp)
					else:output.append(temp)
				except IndexError:
					return False
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

def evaluate(strinput):
	global functions, howManyArgs, function, operator, variables, string
	stack = []
	postfix = shuntingYard(strinput)
	for i in postfix:
		#print stack
		if whatType(i)=="numeric":stack.append(i)
		if whatType(i)=="modifier":stack.append(i)
		if whatType(i)=="identifier": stack.append(variables[i])
		if whatType(i)=="string": stack.append(re.match(string,i).group(1))
		try:
			print stack
			if any((re.match(function,str(i)),re.match(operator,str(i)))):
				args,kwargs=[],[]
				for j in range(howManyArgs[i]):
					args = [stack.pop()] + args
				if(len(stack)>0):
					if whatType(stack[len(stack)-1])=="modifier":
						args = [stack.pop()] + args
				stack.append(functions[i](*args))
		except TypeError:	
			print "KURWA BUONT TYPU"
	if(len(stack)>1):return None
	try:
		return stack[0]
	except IndexError:
		print "BLAD ZWROTU W WYRAZENIU: " + strinput
		raise IndexError
