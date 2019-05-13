#-*-coding:utf8;-*-
#qpy:2
#qpy:console
from __future__ import print_function
from __future__ import division
from collections import Counter as ct
import math
from re import sub
from functools import reduce

#private modules
from lisptypes import xtend,conv
from docs import docstr,helpstr,doclist
import stdlib

#docstr and utils
dbg=False
clog=[]

#compatibility:
try:
  input = raw_input
except NameError:
  pass

#basic working environment
def initmem():
  global mem
  mem={
	 '&':lambda *args:xtend(sum(args)),
	 '*':lambda *args:xtend(reduce(lambda x,y:x*y,args)),
	 ':':stdlib.upgprn,
	 ":'":'strink',
	 ":@":'listconstr',
	 '-':lambda *args:xtend(reduce(lambda x,y:x-y,args)),
	 '/':lambda *args:xtend(reduce(lambda x,y:x/y,args)),
	 '/-':lambda x,y:xtend(x%y),
	 '@':lambda n,arg:arg[n],
	 '@#':lambda x,y:x+[y],
	 '@@':lambda x,y:x+y,
	 '--':lambda x: 0 if x else 1,
	 '**':lambda *args:reduce(pow,args),
	 '!**':math.log,
	 '#-#':range, #change this
	 '@..':lambda *args:list(args),
	 '$$$':stdlib.load,
	 '!?':stdlib.getinp,
  	'###':stdlib.save};mem['+']=mem['&']

global mem
initmem()

#parser and lexer
def parentheses(s):
  c = ct(s)
  if c['('] == c[')']:
    return True
  return False


    
def parse(s):
  if isinstance(s,str):
    s=sub('"([^"]*?)"',lambda x:lisprint(map(ord,list(x.group(1)))),s)
    if s[0]=='(':s=s[1:]
    if s[-1]==')':s=s[:-1]
    s = s.replace('(',' ( ')
    s = s.replace(')',' ) ')
    s = s.split()
  n = []
  for i in s:
    if i!='':
      n.append(i)
  s,b,l = [],0,[]
  for i in n:
    if not b and i not in ['(',')']:
      s.append(conv(i))
    elif i=='(':
      if b:l.append(i)
      b+=1
    elif i==')':
      b-=1
      if not b:
        s.append(parse(l))
        l=[]
      else:
        l.append(i)
    else:
      l.append(conv(i))
  return s

#eval function - syntax definition
def eval(s):
  if isinstance(s,str):
    return mem[s]
  elif s==[]:
    return []
  elif not isinstance(s,list):
    return s
  elif s==["?"] or s==["help"]:
    print(helpstr)
    map(lambda x:print(docstr[x]),doclist)
    return ''
  elif len(s)==2 and s[0]=="?":
    return docstr[s[1]]
  elif s[0]=="'":
    return s[1]
  elif s[0]=='!':
    return map(eval,eval(s[1]))[-1]
  elif s[0]=='!:':
    return map(eval,map(eval,s[1:]))[-1]
  elif s[0]=='?':
    if eval(s[1]):
      return eval(s[2])
    elif len(s)>3:
      return eval(s[3])
  elif s[0]=='!!':
    for mem[s[1]] in eval(s[2]):
      x=eval(s[3])
    return x
  elif s[0] in ['#','=']:
    mem[s[1]]=eval(s[2])
  elif len(s)>2 and s[1] in ['#','=']:
    mem[s[0]]=eval(s[2])
  elif s[0]=='#!':
    mem[eval(s[1])]=eval(s[2])
  else:
    proc=eval(s[0])
    arg=map(eval,s[1:])
    return proc(*arg)

#repl
def lisprint(s):
  if isinstance(s, list):
    return '('+' '.join(map(lisprint,s))+')'
  else:
    return str(s)

print(helpstr)
I,br = True,''
while True:
  I = input('.. ' if br else '>> ')
  if I:br += I
  else:br=''
  if I=='quit':quit()
  if parentheses(br) and br:
    try:
      y = parse(br)
      mem[';@']=y
      x = eval(y)
      mem[';']=x
      clog.append(br)
      print(lisprint(x))
    except Exception as e:
      if dbg: raise
      else: print("Error - "+type(e).__name__+'\n'+str(e))
    br=''
