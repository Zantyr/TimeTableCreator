import re

def branching(exp):
	if(re.match("if ",exp)): return True
	if(re.match("for ", exp)): return True

def rebranching(exp):
	if(re.match("fi",exp)): return True
	if(re.match("rof",exp)): return True

def partialParse(input):
	ret,sub,depth = [],[],0
	for n,i in enumerate(input):
		print depth, i
		exp = (re.match("[\t ]*(.*)",i).group(1))
		if(branching(exp) and n):
			if(not depth): sub=[]
			depth += 1
			sub.append(exp)
		elif(rebranching(exp)):
			depth -= 1
			if(depth):sub.append(exp)
			else:ret.append(partialParse(sub))
		else: 
			if(not depth):ret.append(exp)
			else:sub.append(exp)
	return ret

def parseFile(string):
	tmp = string.split("\n")
	return partialParse(tmp)

with open("script.xD","r") as f:
	print parseFile(f.read())
