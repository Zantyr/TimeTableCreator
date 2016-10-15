################################
#VIRTUAL PYTA MACHINE###########
################################
from collections import Counter as ct
import math
from re import sub
from types import FunctionType

class Int(int):
    def __call__(self, *args):
     if args:
      if isinstance(args[0],FunctionType):
        return args[0](self,*args[1:])
      else:
        return [self]+list(args)
     return [self]
    def __getitem__(self, *args):
      return self
      
class Float(float):
    def __call__(self, *args):
     if args:
      if isinstance(args[0],FunctionType):
        return args[0](self,*args[1:])
      else:
        return [self]+list(args)
     else: return [self]
    def __getitem__(self, *args):
      return self

class List(list):
  def __call__(self, *args):
    if isinstance(self[0],FunctionType):
      return self[0](self[1:]) #here more elaborate evaluation
    

Int.__new__ = int.__new__
Float.__new__ = float.__new__
List.__new__ = list.__new__

def xtend(d):
  if isinstance(d,int): return Int(d)
  elif isinstance(d,float): return Float(d)
  return d

def conv(z):
  try:
    return Int(z)
  except:
    try:
      return Float(z)
    except:
      return z

dbg=False
clog=[]


def upgprn(hwaet, how=None):
   if how==mem[":'"]:
      print(''.join(map(chr, hwaet)))
   else:
      print(lisprint(hwaet))

def getinp(type=None, ln=None):
  if type==mem[":'"] or not type:
    return map(ord,input())
  if type==mem[":@"]:
    I,l=True,""
    while I:
      I=input()
      l+=I
    l=eval(parse(l))
    if not ln:
      return l
    else: return [l[x:x+ln] for x in xrange(0,len(l),ln)]

def pyta_save(machine):
    def save(filelist,content):
        filename='\\'+''.join([x for x in map(chr,filelist)])
        content=''.join([x for x in map(chr,content)])
        machine.save_file(filename,content)
    return save

def pyta_load(machine):
    def load(filelist):
        filename='\\'+''.join([x for x in map(chr,filelist)])
        content = machine.root.get_file(filename).content
        return [x for x in map(ord,content)]
    return load

#basic working environment
def initmem(machine):
  global mem
  mem={
	 '&':lambda *args:xtend(sum(args)),
	 '*':lambda *args:xtend(reduce(lambda x,y:x*y,args)),
	 ':':upgprn,
	 ":'":'strink',
	 ":@":'listconstr',
	 '-':lambda *args:xtend(reduce(lambda x,y:x-y,args)),
	 '/':lambda *args:xtend(reduce(lambda x,y:x/y,args)),
	 '/-':lambda x,y:xtend(x%y),
	 '@':lambda arg,n:arg[n],
	 '@#':lambda x,y:x+[y],
	 '#@':lambda x,y,z:x.__setitem__(y,z),
	 '--':lambda x: 0 if x else 1,
	 '**':lambda *args:reduce(pow,args),
	 '!**':math.log,
	 '#-#':range, #change this
	 '@..':lambda *args:list(args),
	 '$$$':pyta_load(machine),
	 '!?':getinp,
  	'###':pyta_save(machine),
  	'@-#':len,
  	'==':lambda x,y: x==y,
        '!=':lambda x,y: x!=y,
  	};
  mem['+']=mem['&']

global mem

#parser and lexer
def parentheses(s):
  c = ct(s)
  if c['('] == c[')']:
    return True
  return False

def parse(s):
  if isinstance(s,str):
    s=s.strip()
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
  elif s[0]=='?..':
    while(eval(s[1])):
      x=eval(s[2])
    return x
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

def pyta(machine,source):
    initmem(machine)
    y = parse(source)
    try:
        x = eval(y)
    except Exception as e:
        print("PytaError: "+type(e).__name__+" : "+str(e))
    return lisprint(x)
