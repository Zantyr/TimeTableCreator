import re

def branching(exp):
	if(re.match("dopoki ",exp)): return True
	if(re.match("jesli ", exp)): return True
	if(re.match("definicja ", exp)): return True
def rebranching(exp):
	if(re.match("ilsej",exp)): return True
	if(re.match("ikopod",exp)): return True
	if(re.match("ajcinifed", exp)): return True

def partialParse(input):
	ret,sub,depth = [],[],0
	for n,i in enumerate(input):
		if not i: continue
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
