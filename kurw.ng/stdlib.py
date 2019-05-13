#compatibility
try: input=raw_input
except NameError: pass

def save(filenum):
  with open(str(filenum)+'.ng','w') as f:
    for i in clog:
      f.writeline(i)

def load(filenum):
   with open(str(filenum)+'.ng','r') as f:
    for i in f:
     try:
      y = parse(i)
      mem[';@']=y
      x = eval(y)
      mem[';']=x
      clog.append(i)
      print(lisprint(x))
     except Exception as e:
      if dbg: raise
      else: print("Error - "+type(e).__name__+'\n'+e.message)

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

def crreg(*args):
   x,y=zip(*args)
   sx,sy=sum(x),sum(y)
   sxy=sum(map(lambda a:a[0]*a[1],args))
