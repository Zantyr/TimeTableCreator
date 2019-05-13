#This program is made to take partial control of the computer it is installed on. The clue is to make it a computational bot for your own purposes
#Of course to make it more useless and more educational all commands are implemented through a brand new interpreted scriptlang.
#Enjoy - MindSlaver - 2016, Zantyr
#DoWhatTheFuckYouWant License 1.0

#################################
##  TABLE OF CONTENTS:         ##
##  0. Preloading              ##
##  1. Expression evaluator    ##
##  2. Script parser           ##
##  3. Flow-control            ##
##  4. Main Loop               ##
#################################

#import built-in modules
import os
import re

#import settings
from defs import * 

#append modules
import builtIns

########################
##Expression evaluator##
########################

#TO DO: check this function
def isList(i):
	try:
		y = i.pop()
		i.append(y)
		return True
	except AttributeError:
		return False

#TO DO: upgrade this function to make something that makes sense
#this checks the type of input
def whatType(arg):
	try:
		x = 2.0  + arg
		return "numeric"
	except TypeError:
		try:
			if(re.match(token_string,arg)): return "string"
			elif(re.match(token_identifier,arg)): return "identifier"
			elif(re.match(token_function,arg)): return "function"
			elif(re.match(token_modifier,arg)): return "modifier"						
			else: return None
		except TypeError:
			if(isList(arg)): return "list"
			else: return None

#this checks associativity of tokens
def assoc(i):
	left=["+","-","*","/"]
	if i in left: return True
	else: return False

#this checks whether to pop tokens from stack or not
def precedence(i,j):
	pre = {'<=': -1, '>=': -1, '>>': -1, ')': 99, '(': -4, '+': 1, '*': 2, '-': 1, '/': 2, '==': -1, '!=': -1, '<<': -1, '^': 3}
	#PRECEDENCE OF FUNCTIONS
	if((pre[i]<=pre[j] and assoc(i)) or (pre[i]<pre[j] and assoc(i))): return True
	else: return False

#this function splits the string without splitting quoted strings
def upgradedSplit(asc):
	#TO ADD: adding spaces in expressions to split it without need of the user to use spaces everywhere (though the code looks nice)
	replace = []
	while(re.search(token_string,asc)): #this replaces the strings in expression with replacer tokens as long as possible
		s = re.search(token_uprgraded_split_string,asc)
		asc = s.group(1)+"!&@"+str(len(replace))+s.group(3)
		replace.append(s.group(2))
	ret = asc.split(" ")
	for i in xrange(len(replace)): #this replaces the replacers with strings BACK 
		for n,el in enumerate(ret):
			if el=="!&@"+str(i):
				ret[n] = replace[i]
	return ret


#shuntingYard algorithm
#converts infix notation to postfixm which is easier to evaluate
def shuntingYard(strin):
	#TO DO: precompile regexp, to not compile them everytime you use them
	global operator, numeric, function, identifier, separator, string #import regexp markers for various tokens
	left = "\("
	right = "\)"
	output,stack = [],[] #output list is a ready infix, stack is for storing operator/function/parenthesis tokens
	tokens = upgradedSplit(strin) #split the string to a list of tokens
	for token in tokens:
		x = re.match(token_numeric,token)
		if(x): 
			#TO ADD: converting to ints or longs IF POSSIBLE
			output.append(float(x.group(1)))
			continue
		x = re.match(token_string,token)
		if(x): 
			output.append(x.string)		
			continue
		x = re.match(token_identifier,token)		
		if(x): output.append(x.group(1))
		x = re.match(token_function,token)
		if(x): stack.append(x.group(1))
		x = re.match(token_separator,token)
		if(x): #DAFUQ
			temp = ""
			while(temp!="("):
				try:
					temp = stack.pop()
					if(temp=="("): stack.append(temp)
					else:output.append(temp)
				except IndexError:
					return False
		x = re.match(token_operator,token)
		if(x):
			while(len(stack)): #pops all tokens from stack with lower precedence that the current token 
				if(precedence(token,stack[-1])):output.append(stack.pop()) 
				else: break
			stack.append(token)#add the current token
		x = re.match(left,token)
		if(x): stack.append("(")
		x = re.match(right,token) #DAFUQ 2.0
		if(x):
			while(len(stack)):
				temp = stack.pop()
				if(temp=="("):
					stack.append(temp)
					if(len(stack)):
						temp = stack.pop()
						if re.match(token_function,temp): output.append(temp)
					break
				else:
					output.append(temp)
	stack.reverse() # pop all remainding tokens
	output += stack
	if (("(" in output) or (")" in output)): return False #TO DO: raise an error
	else: return output

#this function evaluates the infixed expression
def evaluate(strinput):
	stack = []
	postfix = shuntingYard(strinput) #magic happens (look above for infix-postfix wonder)
	for i in postfix:
		if whatType(i)=="numeric":stack.append(i)
		elif whatType(i)=="modifier":stack.append(i);
		elif whatType(i)=="identifier": stack.append(variables[i]);
		elif whatType(i)=="string":
			if(i[0]==i[-1]=="\""):
				stack.append(i[1:-1]);
		else:
			try:
				if(VERBOSE): print stack #FOR FUCKING DEBUG PURPOSES
				if any((re.match(token_function,str(i)),re.match(token_operator,str(i)))):
					args=[]
					for j in xrange(howManyArgs[i]): #may raise error due to lack of args
						args = [stack.pop()] + args
					if(len(stack)):
						if whatType(stack[-1])=="modifier": args.append(stack.pop()) #add optional modifer to args 
					stack.append(functions[i](*args)) #call function and append the output
			except TypeError:	#please, reevaluate which errors may be raised
				print "KURWA BUONT TYPU"
	if(len(stack)>1):return None #TO DO: Raise an Error!
	try: #TO DO: Raise an Error!
		return stack[0]
	except IndexError:
		print "BLAD ZWROTU W WYRAZENIU: " + strinput
		raise IndexError

##########
##PARSER##
##########

#checks if something is on list
def ifOnList(exp,applicable):
	for x in applicable:
		if(re.match(x,exp)): return True
	return False

#this recursively parses lists to form a LISP-like tree of lists
def partialParse(input):
	ret,sub,depth = [],[],0
	for n,i in enumerate(input):
		if not i: continue
		exp = (re.match("[\t ]*(.*)",i).group(1))
		if(ifOnList(exp,keyword_branching) and n):
			if(not depth): sub=[]
			depth += 1
			sub.append(exp)
		elif(ifOnList(exp,keyword_rebranching)):
			depth -= 1
			if(depth):sub.append(exp)
			else:ret.append(partialParse(sub))
		else: 
			if(not depth):ret.append(exp)
			else:sub.append(exp)
	return ret

#splits the string line by line and parses it
def parseFile(string):
	tmp = string.split("\n")
	return partialParse(tmp)

######################
##SCRIPT INTERPRETER##
######################

#this evaluates an assignment expression
def assign(string):
	global variables
	x = re.match("([A-Za-z_](\w)*) ?= ?(.*)",string)
	if(x): variables[x.group(1)] = evaluate(x.group(3))
	else: return False

#this constructs a subroutine
def constructor(lista):
	def func(*args):
		run(lista)
		return
	return func

#RUN FUNCTION
#this executes the list of parsed commands and takes care of flow control
def run(lista,listener=None):
	if(VERBOSE):print lista #debug
	global variables
	if listener: IOsets["listener"]=listener #checks the listener
	for n,j in enumerate(lista):
		i = str(j)
		if(VERBOSE): print n, i  #debug
		if(re.match(syntax_assignment,i)): assign(i)
		elif(re.match(syntax_call,i)): evaluate(i)
		elif(re.match(syntax_return,i)): return variables[variable]
		elif(isList(j)): #inline lists - flow control
			x =re.match(syntax_defun,j[0]) #creates a new function and links the function
			if x:
				functions["!"+x.group(1)] = constructor(j[1:])
				howManyArgs["!"+x.group(1)] = 0
			x =re.match(syntax_while,j[0]) #runs a WHILE loop
			if x:
				while(evaluate(x.group(1))): 					
					y = run(j[1:])
					if y != None: return y
			x =re.match(syntax_conditional,j[0])  #runs an IF condition
			if x:
				if(evaluate(x.group(1))): 					
					y = run(j[1:])
					if y != None: return y
	return
########
##MAIN##
########

#clear console
os.system('cls' if os.name=='nt' else 'clear')
with open(DEFAULTSCRIPT,"r") as f:
	asc =  f.read()
run(parseFile(asc))
