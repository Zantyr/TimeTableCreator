#todo: convert ints to ints on the list, floats to floats and upgrade type handling
#add variables and type handling
#add "CTRL ?+ ?F (.*)" command

#prerequisite libraries
import re

#helpful vars and consts
from script import variables
from script import functions
from script import howManyArgs
from script import IOsets
from operators import *
from builtIn import *
from shunting import evaluate

#operators
import operators
import shunting

#external functions
import connect

#this algorithm evals everything
	

def assign(string):
	global variables
	x = re.match("([A-Za-z_](\w)*) ?= ?(.*)",string)
	if(x): variables[x.group(1)] = evaluate(x.group(3))
	else: return False

def stdout(variable):
	global variables
	print variables[variable]

def isList(i):
	try:
		y = i.pop()
		i.append(y)
		return True
	except AttributeError:
		return False

def constructor(lista):
	def func(*args):
		run(lista)
		return
	return func

def run(lista,listener=None):
	print lista
	global variables
	global functions
	global howManyArgs
	global IOsets
	if listener: IOsets["listener"]=listener
	for n,j in enumerate(lista):
		i = str(j)
		#print n, i  #komentowalne, do debugu
		if(re.match("([A-Za-z_](\w)*) ?= ?(.*)",i)): assign(i)
		elif(re.match("![A-Za-z_](\w)*",i)): evaluate(i)
		elif(re.match("return [A-Za-z_](\w)*",i)): return variables[variable]
		elif(isList(j)):
			first =re.match("definicja ([A-Za-z_](\w)*)",j[0]) 
			if first:
				functions["!"+first.group(1)] = constructor(j[1:])
				howManyArgs["!"+first.group(1)] = 0
			first =re.match("dopoki (([^n]*))",j[0]) 
			if first:
				while(evaluate(first.group(1))): 					
					y = run(j[1:])
					if y != None: return y
			first =re.match("jesli (([^n]*))",j[0]) 
			if first:
				if(evaluate(first.group(1))): 					
					y = run(j[1:])
					if y != None: return y
		else:
			x = re.match("wykurw",i)
			if(x):
				print "WYJEBUJE..."
				for i in variables: print i + " : " + str(variables[i])
	return
