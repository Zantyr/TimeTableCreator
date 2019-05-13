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
