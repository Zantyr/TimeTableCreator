#-*- coding: utf-8; -*-
from __future__ import print_function
import re
from sys import argv

def print_default(machine,match):
    if match.lower()=="zaburzenia emocjonalne": print(str(machine.stack.pop()))
    else: print(match)

def listen_default(machine,match):
    if match.lower()=="włos" or match.lower()=="wlos": machine.stack.append(raw_input("Co słyszy Magik: "))
    else:
        machine.memory[match] = raw_input("Co słyszy Magik: ")

DEFAULT_TRANSFORM = {
r"(.*) na mikrofonie":lambda x:(lambda x,y:print(x.memory[y]),x[0]),
r"Powiesz mi,? (?:z|ż)e to (.+), powiem Ci,? (?:z|ż)e to (.+)":lambda x:(lambda x,y,z:x.memory.__setitem__(y,z),x[0],x[1]),
r"Mam jeden pierdolony (.*)":lambda x:(lambda x,y:x.stack.append(x.memory[y]),x[0]),
r"Mam jedn(?:a|ą) pierdolon(?:a|ą) (.*)":lambda x:(lambda x,y:x.stack.append(x.memory[y]),x[0]),
r"Mam jedno pierdolone (.*)":lambda x:(lambda x,y:x.stack.append(x.memory[y]),x[0]),
r"(.*) - prosz(?:e|ę) pu(?:sc|ść) to na antenie":lambda x:(print_default,x[0]),
r"s(?:l|ł)ysz(?:e|ę) s(?:l|ł)owa,? od kt(?:o|ó)rych (.*) je(?:ż|z)y si(?:ę|e) na g(?:ł|l)owie":lambda x:(listen_default,x[0]),
r"Bo w tym kraju ka(?:z|ż)d(?:a|e|y) (.*) to jest (.*)":lambda x:(lambda x,y,z:x.stack.append(x.stack.pop().replace(y,z)),x[0],x[1]),
r"Od teraz(?: jest)? to (.*?)(?:| - .*|, .*)$":lambda x:(lambda x,y:x.memory.__setitem__(y,x.stack.pop()),x[0]),
r"M(?:ó|o)wię, (?:ż|z)e mam tu ma(?:ł|l)y dysonans":lambda x:(lambda x: x.stack.append([x.stack.pop()]!=[x.stack.pop()]),),
r"(.*) i (.*) to jedyne, co widz(?:e|ę)":lambda x:(lambda x,y,z:(x.stack.append(x.memory[y]) or x.stack.append(x.memory[z])),x[0],x[1]),
}

class Function(object):
    def __init__(self,function=None):
        self.function = function
    def __call__(self,machine,*args,**kwargs):
        scope = machine.stack
        return self.function(*args,**kwargs)

class BuiltFunction(Function):
    pass

class RapMachine(object):
    #built-in
    def __init__(self,files=("elorap.xd"),debug=False):
        self.debug=debug
        self.stack = []
        self.memory = {}
        self.regex_transform = DEFAULT_TRANSFORM
        self.calls = {'import':self._build_rhymes}
    #public
    def run(self,code):
        self._execute_rap_code(self._parse_string(code))
    def docs(self):
        print("No docs")
    #private
    def _rhymes(self,x):
        return False
    def _parse_string(self,s):
        #divide to stanzas
        s = re.sub("\/\/(.*)","\1",s)
        s=[x.strip() for x in s.replace('\r\n','\n').split('\n\n')]
        #check rhymes
        if any([self._rhymes(x) for x in s]): raise SyntaxError
        #parse to rapcode
        r=[]
        [r.extend(self._stanza(x)) for x in s]
        return r
    def _execute_rap_code(self,c):
        """
        executes all command passing
        """
        if self.debug: print(c)
        for i in c:
            i[0](self,*i[1:])
    def _stanza(self,c):
        """
        returns commands a la (call,value,value...)
        """
        try:
            stanza = []
            for s in (y.strip() for y in c.split('\n')):
                for transform in self.regex_transform:
                    x = re.match(transform,s,flags=re.IGNORECASE)
                    if x != None:
                        stanza.append(self.regex_transform[transform](x.groups()))
                        break
            return stanza
        except KeyError:
            return SyntaxError #gotta fix
    def _build_rhymes(self):
        pass

if __name__=='__main__':
    try:
        if argv[1]=='help':
            RapMachine().docs()
            quit()
        else:
            DEBUG=False
            if argv[1]=='--debug':
                DEBUG=True
                filename=argv[2]
            else:
                filename=argv[1]
            with open(filename,"r") as f:
                s = f.read()
    except IndexError:
        print("Pass filename to open and execute, or <<help>> to get to the docs\n--debug enables debug logs")
        quit()
    except IOError:
        print("File does not exist!")
        quit()
    RapMachine(debug=DEBUG).run(s)
