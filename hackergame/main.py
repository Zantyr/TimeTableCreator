from __future__ import print_function
from __future__ import division

"""
.hwdp
3th server contains bdsm instructions and keygen to final archive in a broken archive
4th server contains password breaker and scp command docs and some broken archives and link to 8,9
5th server has decoded folder and protected archive_fixer(which will require some work to work right, e.g. license key)
6th server has a folder_decoder(permissions) and all passwords and licenses in a base64 file
7th server contains broken YOUWIN.xD and license to archive_repairer
8th server contains instructions how to fix it, in a broken pyta script in an encoded archive
"""

#JEBANA GRA DLA BRATA
from time import sleep
try: input=raw_input
except NameError: pass

#manual
MAN={'pyta':"""\nPyta programming language\nUnstable and experimental\nFeatures may not work correctly\n\nOverall syntax:\n(a b c ...) => a(b,c,...)\n\nSyntax tips:\n(' x)     - return x unevaluated\n(# x y)   - set uneval x to y\n(#! x y)  - set evalled x to y\n(! x)     - execute list x, ret last\n(!: ...)  - execute unpacked list\n(? x y)   - if x execute y\n(? x y z) - if x then y else z\n\nCommands:\n'&': sum the arguments\n'*': multiply the arguments\n'-': subtract\n'/': division\n'/-': modulo\n':': print (accepts :' as a parameter to print strings)\n'@': access the nth element of a list\n'@#': append argument to list\n'#@': x[y]=z\n'--': negate\n'**': power\n'!**': logarithm\n'#-#': range(may not work)\n'@..': list from args\n'$$$': load file\n'!?': get input :' for strings\n'###': save file\n""",'man':"""This is GNU manual page\n\nYou may want to find some help there.\njust type 'man <topic>'\nGood luck\n\nUseful commands: ls, cd, dog, pyta, ssh, lgbt, chmod, mkdir, rm""",'ls':"Log out. Seriously.\nThis actually shows only the current folder.",'cd':"This varies from normal cd: there's no ..","lgbt":'Low Grade Budget Text-editor\nUnlike vim has only command mode\n+:text appends text\n+:number inserts a line\n-:number removes a line\n?:number shows a scope\n? shows whole document\nnumber:text replaces the given line with the text\nquit - quits ofc','dog':'This is the plain old cat. Copyleft, all rights reversed.','nmap':'This actually requires no parameters. Instead, it needs root access.','scp':'One-way copy through ssh\nusage:scp host localsource remotetarget\nlocally uses $PWD','chmod':'This chmod has cow super-powers','bdsm':'BADLY DESIGNED SCRIPTING MACHINE\n\nBudget version of apt-get\nbdsm <name> either runs a script or installs it if key is available','mkdir':'www.google.com','rm':'Removes an element, either file or folder. Doesn\'t do it recursively.'}

def archive_manager(machine):
    print("This is the Heavily Wicked Disposer of Packages")
    archivename = '\\' + input('Give me filename: ')
    archive = machine.root.get_file(archivename)
    if(archive.perms()[0] != 'r'):
        print('You cannot read this')
        return
    archive = archive.content.decode('base64')
    archive = json.loads(archive)
    if archive['password'] != '':
        pw = input('This archive is protected. Enter the password')
        if pw != archive['password']:
            print('Wrong password. Termin@ting...')
            return
    for i in archive:
        machine.save_file(archivename+i,archive[i])
    machine.save_folder(archivename)

def password_breaker(machine):
    print("by HAXX0R team\n\nThis is...\n+-      |      +-,            |\n| \\    -+-  -  | |         -  |\n+-/ | | |    \\ +<  | /,-,   \\ | /\n|   | | |  ,-+ | | |/ |-' ,-+ |<\n|   \\_/ \\_ '-+ +-' |  \\_  '-+ | \\\n     /\n    -\n")
    archivename = input('Give me filename: ')
    archive = machine.root.get_file('\\' + archivename)
    if(archive.perms()[0] != 'r'):
        print('You cannot read this')
        return
    archive = archive.content.decode('base64')
    archive = json.loads(archive)
    print(archive['password'])

def victory_script(machine):
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    print("YOU JUST WON THE GAME")
    print("HEPI BERFDEJ KURWA")

BDSM_REPOS={"bdsm.tar.gz.archive.manager,key:DB A2 38 40 C9 3B":('hwdp',archive_manager),
            "bdsm.http.win.the.game:03 05 08 0D 15 22":('win',victory_script),
            "bdsm.util.java.lang.jvm-to-pyta.modules.pytabreak: 56 AA C4 56 AA C4":('pytabreak',password_breaker)}

class File(object):
    def __init__(self,content="",perms=(True,True,False)):
        self.content=content
        self.__perms = list(perms)
    def perms(self):
        return ("r" if self.__perms[0] else "-")+("w" if self.__perms[1] else "-")+("d" if self.__perms[2] else "-")
    def unlock(self):
        self.__perms[0] = True
        self.__perms[1] = True

class Folder(File):
    def __init__(self,name,root,perms=(True,True,True)):
        self.name = name
        self.root = root
        self.__perms = list(perms)
    def get_files(self):
        return self.root.get_files(self.name)
    def perms(self):
        return ("r" if self.__perms[0] else "-")+("w" if self.__perms[1] else "-")+("d" if self.__perms[2] else "-")
    def unlock(self):
        self.__perms[0] = True
        self.__perms[1] = True

class App(File):
    pass

class Root(Folder):
    def __init__(self,memory=None):
        self.memory = {} if not memory else memory
    def get_file(self,name):
        if name=='\\':
            return self
        else:
            return self.memory[name]
    def get_files(self,name=None):
        dictionary = {}
        if name!=None:
            for key in self.memory:
                if(key[:len(name)+1]==name+"\\" and '\\' not in key[len(name)+1:]):
                    dictionary[key] = self.memory[key]
        else:
            for key in self.memory:
                if('\\' not in key[1:]):
                    dictionary[key] = self.memory[key]
        return dictionary

class Machine(object):
    """
    Has filesystem (root), shows sh(...) that acts as a shell, has also network_env
    """
    def __init__(self,ip_address,password,iso=None):
        if iso:
            self.root = Root(iso)
        else:
            self.root = Root()
        self.env = {"$PWD":'\\'}
        self.calls = {'ls':self.__ls,'man':self.__man,'help':lambda *x:print("No such command, man"),'cd':self.__cd,'pyta':self.__pyta,'ssh':self.__ssh,'scp':self.__scp,'dog':self.__dog,'lgbt':self.__lgbt,'bdsm':self.__bdsm,'nmap':self.__nmap,'chmod':self.__chmod,'mkdir':self.__mkdir,'rm':self.__rm}
        self.sudo_password = password
        self.ip_address = ip_address
        self.network={self.ip_address:self}
        self.motd = "Hello in cra.sh OS\nversion 1.0.3 build nightly\nMachine: "+self.ip_address+"\n\n"
        self.bye = "Disconnected from "+self.ip_address
    def sh(self,is_main=False):
        print(self.motd)
        while True:
            try:
                cmd = input(self.env['$PWD']+" >> ")
                if cmd.lower()=="exit":
                    if is_main:
                        cmd = input(self.env['$PWD']+"Retype 'exit' to quit the game (IT CANNOT BE SAVED!): ")
                        if cmd.lower()=="exit":
                            break
                    else: break
                else:
                    cmd = cmd.split(' ')
                    try:
                        command = self.calls[cmd[0]]
                        try:
                            command(*cmd[1:])
                        except Exception as e:
                            print("SHELL FAULT: "+type(e).__name__)
                    except KeyError:
                        print("No such command")
            except KeyboardInterrupt:
                print("Log out to quit the game.")
        print(self.bye)
    def sys(self,call):
        return self.calls[call]()
    def __cd(self,*args):
        if not args:
            self.env['$PWD']="\\"
        else:
            try:
                assert(self.root.get_file(self.env["$PWD"]+("\\" if self.env["$PWD"]!="\\" else "")+args[0]).perms()[2] == 'd')
            except KeyError:
                print("No such folder")
                return
            except AssertionError:
                print("Is a file")
                return
            try:
                assert(self.root.get_file(self.env["$PWD"]+("\\" if self.env["$PWD"]!="\\" else "")+args[0]).perms()[0] == 'r')
                self.env["$PWD"]=self.env["$PWD"]+("\\" if self.env["$PWD"]!="\\" else "")+args[0]
            except AssertionError:
                print("No read permissions to enter this folder")
    def __chmod(self,*args):
        if not args: 
            print("Pass actual file")
            return
        pw = input("Root access is needed: ")
        if pw==self.sudo_password:
            self.root.get_file(self.env["$PWD"]+("\\" if self.env["$PWD"]!="\\" else "")+args[0]).unlock()
        else:
            sleep(2)
            print("Incorrect password")
    def __ls(self,*args):
        try:
            file = self.root.get_file(self.env["$PWD"]+(("\\"+args[0]) if args else ""))
            try:
                files = file.get_files()
                string = ""
                for key in files:
                    string += ("\n" if string else "") + files[key].perms() + " " + key[1:].split('\\')[-1]
                print(string)
            except:
                raise
                print("Not a folder")
        except KeyError:
            print("No such folder")
    def __man(self,*args):
        if not args:
            print(MAN['man'])
        else:
            print(MAN[args[0]])
    def __pyta(self,*args):
        if not args:
            print("Give an input file")
            return
        try:
            file = self.root.get_file(self.env["$PWD"]+("\\" if self.env["$PWD"]!="\\" else "")+args[0])
            if(file.perms()[0]=='r'):print(pyta(self,file.content))
            else:print("Cannot read this file")
        except KeyError:
            print("No such file")
    def __ssh(self,*args):
        if not args:
            print("Pass address")
        try:
            host=self.network[args[0]]
            pw=input("Password: ")
            if pw==host.sudo_password:
                host.sh()
            else: print("Wrong password")
        except KeyError:
            sleep(3)
            print("No such host")
    def __scp(self,*args):
        if len(args)<3:
            print("Pass correct amount of arguments")
        try:
            host=self.network[args[0]]
            pw=input("Password: ")
            if pw==host.sudo_password:
                try:
                    file = self.root.get_file(self.env["$PWD"]+("\\" if self.env["$PWD"]!="\\" else "")+args[1])
                    if(file.perms()[0]=='r'):
                        host.save_file(args[2],file.content)
                    else:print("Cannot read this file")
                except Exception:
                    print("Failure. Aborting.")
            else: print("Wrong password")
        except KeyError:
            sleep(3)
            print("No such host")
    def __dog(self,*args):
        if not args:
            print("Give an input file")
            return
        try:
            file = self.root.get_file(self.env["$PWD"]+("\\" if self.env["$PWD"]!="\\" else "")+args[0])
            if(file.perms()[0]=='r'):print(file.content)
            else:print("Cannot read this file")
        except KeyError:
            print("No such file")
    def __lgbt(self,*args):
        if not args:
            buffer = ""
        else:
            try:
                file = self.root.get_file(self.env["$PWD"]+("\\" if self.env["$PWD"]!="\\" else "")+args[0])
                try:
                    assert(file.perms()[:2]=="rw")
                    buffer = file.content
                except AssertionError:
                    print("Cannot open the file - permission to read and write denied")
                    return
            except KeyError:
                print("No such file")
                return
        print("Welcome to Low Grade Budget Text-editor\nI hope you've read man, cause there's no help\n")
        buffer = buffer.split('\n')
        while True:
            cmd = input(str(len(buffer))+" >> ")
            if cmd=='quit':
                break
            cmd = cmd.split(':',1)
            try:
                if cmd[0]=='+':
                    try:
                        i = int(cmd[1])
                        buffer=buffer[:i]+[""]+buffer[i:]
                    except:
                        buffer.append(cmd[1])
                elif cmd[0]=='-':
                    i = int(cmd[1])
                    buffer=buffer[:i]+buffer[i+1:]
                elif cmd[0]=='?':
                    try:
                        i = int(cmd[1])
                        print('\n'.join(buffer[i-1:i+24]))
                    except IndexError:
                        print('\n'.join(buffer))
                else:
                    i = int(cmd[0])
                    buffer[i-1]=cmd[1]
            except:
                print("Syntax Error")
        buffer = '\n'.join(buffer)
        if not args:
            args = [input("Give me the filename: ")]
        self.save_file(self.env["$PWD"]+("\\" if self.env["$PWD"]!="\\" else "")+args[0],buffer)
    def __bdsm(self,*args):
        if not args:
            print("BDSM Fataler Fehler: keine Skript gewahlt.")
            return
        try:
            func = self.env[args[0]]
        except KeyError:
            try:
                key = self.root.get_file(self.env["$PWD"]+("\\" if self.env["$PWD"]!="\\" else "")+args[0]).content
                print("Das Skript aus dem Rep erhalten")
                sleep(3)
                cmd,func = BDSM_REPOS[key]
                print("Installieren...")
                self.env[cmd] = func
                sleep(4)
                print("Fertig, kurwa.")
                print("Befehl fur dieses Skript ist: "+cmd)
                return
            except KeyError:
                print("BDSM Fataler Fehler: das Skript nicht verfugbar")
                return
        try:
            func(self)
        except Exception as e:
            print("BDSM Fataler Fehler: "+type(e).__name__)
    def __nmap(self,*args):
        pw = input("Root access is needed: ")
        if pw==self.sudo_password:
            print("Checking the networks...")
            sleep(17)
            for i in self.network:
                print(i+" - host is up!")
        else:
            sleep(4)
            print("Segmentation fault")
    def __mkdir(self,*args):
        if not args:
            print("Give an input file")
            return
        self.save_folder(self.env["$PWD"]+("\\" if self.env["$PWD"]!="\\" else "")+args[0])
    def __rm(self,*args):
        if not args:
            print("Give an input file")
            return
        self.root.memory.pop(args[0])
    def save_file(self,abs_name,content="",permissions=(True,True,False)):
        self.root.memory[abs_name] = File(content,permissions)
    def save_folder(self,abs_name,permissions=(True,True,True)):
        self.root.memory[abs_name] = Folder(abs_name,self.root,permissions)
    def add_connection(self,machine):
        self.network[machine.ip_address] = machine
        machine.network[self.ip_address] = self

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

######
#main

if __name__=="__main__":
    machine = Machine('192.168.0.5','cipka')
    machine.save_folder("\\secret",(False,False,True))
    machine.save_folder("\\home")
    machine.save_folder("\\home\\ruchacz")
    machine.save_folder("\\home\\zantyr")
    machine.save_file("\\home\\zantyr\\YOUWIN.ng","(?.. 1 (: \"xDD\" :'))")
    machine.save_file("\\home\\ruchacz\\riddle.ng","(!: (# $iter 0) (# $list \""+'Ok\x1cukq\x1c`a_eldana`\x1cpdeo\x1codep***\x1cPdana\x1ceo\x1c]\x1cne``ha\x1cbkn\x1cukq\x1cpk\x1cokhra(\x1cjecc]6\x1cPda\x1cnkkp\x1cl]ooskn`\x1cbkn\x1cpdeo\x1cbna]gejc\x1ci]_deja\x1ceo\x1cpda\x1cj]ia\x1ckb\x1c^kpd\x1cpda\x1cpdejc\x1cukq\x1chega\x1cpda\x1c^aop\x1c]j`\x1cpda\x1c_qpa\x1cheppha\x1c]jei]h\x1cpd]p\x1cd]pao\x1cpda\x1cpdejco\x1cpd]p\x1c^]ng*\x1cPn]joh]pa\x1cep\x1cpk\x1clkheod*\x1cCkk`\x1chq_g\x1d\x1c=hok***\x1cukq\x1ci]u\x1cqoa\x1cpdeo\x1cpkkh\x1c$eb\x1cukq\x1cik`ebu\x1cep%\x1cpk\x1c`a_eban\x1cpda\x1cl]ooskn`*\x1cPdeo\x1ceo\x1cep6\x1cSY`[Q'+"\") (?.. (!= $iter (@-# $list)) (!: (#@ $list $iter (& (@ $list $iter) 4)) (# $iter (& $iter 1)) )) (### \"data.out\" $list) (: \"Done.\" :\') )")
    machine.save_file("\\home\\ruchacz\\incaseyoureloser.txt","Hi! If you fail to own this riddle, there's another way to get the password. Just go to the root folder and type in 'dog oh\\my\\god\\i\\am\\a\\fucking\\loser.txt' ")
    machine.save_file("\\objective.txt","Hi!\n\nThis is the key to your destiny.\nThis is epic journey to acquire your legacy.\nThis is the way to mastery.\n\nThis is your birthday present, the Ruchacz One.\n\nAs you approach you maturity, you will have to pass a series of tests.\nDon\'t worry, they\'re easy for a skilled programmer like you!\n\nYou\'r objective is to: open the file in secret folder and retrieve password to your present.\n\nGood luck!",(True,True,False))
    machine.save_file("\\secret\\tool.ng","(!: (: \"This tool is a fucking glorious tool to perform arbitrary caesar-like shift on ASCII\" :') (# $shift 4) (# $iter 0) (# $list ($$$ \"data.in\")) (?.. (!= $iter (@-# $list)) (!: (#@ $list $iter (& (@ $list $iter) $shift)) (# $iter (& $iter 1)) )) (### \"deciphered.out\" $list) (: \"Done.\" :\') )")
    machine.save_file("\\secret\\YOUWIN.txt","Hi! You own it!\n\nUnfortunately princess is in another castle. There\'s file called \'briefing.txt\' somewhere on a distant server on Bahama island. Retrieve this file and you will obtain glory and pussy.",(False,False,False))
    machine.save_file("\\objective.txt","Hi!\n\nThis is the key to your destiny.\nThis is epic journey to acquire your legacy.\nThis is the way to mastery.\n\nThis is your birthday present, the Ruchacz One.\n\nAs you approach you maturity, you will have to pass a series of tests.\nDon\'t worry, they\'re easy for a skilled programmer like you!\n\nYou\'r objective is to: open the file in secret folder and retrieve password to your present.\n\nGood luck!",(True,True,False))
    machine.save_file("\\fairplay.txt","This game is to played fair. No use of python, no copy-paste from the terminal. You may use internet to search for things. DO NOT EVER LOOK AT THE SOURCE CODE!",(True,True,False))
    machine.save_file("\\oh\\my\\god\\i\\am\\a\\fucking\\loser.txt","cipka")
    machine.motd=machine.motd+"Such a great day for birthday present!\n\n"
    machine.save_folder("\\secret\\RSA")
    machine.save_file("\\secret\\RSA\\keygen.ng","(!: (# $iter 0) (# $list \""+'Gauo\x1cbkn\x1cji]l6\x06-5.*-24*-*-01\x1co]epk_dqf\x06-5.*,*,*,\x1c^h]vaep'+"\") (?.. (!= $iter (@-# $list)) (!: (#@ $list $iter (& (@ $list $iter) 4)) (# $iter (& $iter 1)) )) (: $list :') (: \"Done.\" :\') ))")

    #second phase

    second_machine = Machine("192.168.0.145",'saitochuj')
    third_machine = Machine("192.0.0.0",'blazeit')
    #FURTHER INSTRUCTIONS
    second_machine.save_file("\\dev\\YOUWON.txt","dobry wieczor cos sie popsulo i nie bylo mnie slychac i powtorze jeszcze raz wynik wyborczy kww stonogi to jest jakas porazka ja mysle ze to polskie kurwa glupie spoleczenstwo te kurwa banda inbecyli ktora glosowala na tych kurwow karakanow z pisu to jest jakies kurwa nieporozumienie jesli tyle dla was znaczy jesli tyle dla was znaczy ludzie takie zangaaa takie zangazowanie spoleczne jak moje gdzie postawilem moja rodzine moje zycie prywatne biznes wszystko inne i dla was znaczylo to tylko 70 czy 80 tysiecy glosow to was sie powinno jebac kurwa tak sie powinno was jebac jak tylko was moze jebac pis platforma was tak nie wyruchala jak wyrucha was pis kurwa az was kukle beda swedzialy z bolu to jest dramat kurwa to jest dramat ze w tym antyludzkim panstwie w tym panstwie w ktorym media kurwa nie byly w stanie powiedziec ze zbigniewa stonoge zbezszczeszczono ze ten czlowiek ma 118 wyrokow uniewinniajacych ze te sadowe kurwy powtarzam kurwy sadowe kurwy tego czlowieka oskarzaly bezpodstawnie i po latach uniewinnialy ze to nie jest czyms wartym tego by tego czlowieka wprowadzic do parlamentu bedzie was pis ruchal w dupe bedzie was pis bedzie kurwa dymal tak jak was platforma nie dymala ta kurwa ten maly karakan jebany kaczynski smiec zniszczy was sumlinskie kanie lachonie telewizje republiki beda wam kurwa odbieraly smak zycia wy kurwa idioci narodowi polscy idioci ja mam to w pizdzie kurwa bo mnie stac na wszystko bede zyl kurwa tak wypierdole jeszcze dzisiaj juz bilet kupiony z polski password to sixth server is tool i bede sie z was kurwa frajery smial ze wy takie glupie sa tacy kurwa debile ktore to kurestwo pisowskie wybrali nie na korwina nie na stonoge tylko na jakies kurwy petru zydow w dupe jebanych kurwa na kukizow popierdolencow glosowalito jest ta wlasnie kurwa polska przez taka kurwe polske przez was kurwa chuje nic sie w tym kraju nie zmieni bo jestescie chuj warci i trzeba was jebac ruchac i na was zarabiac bo jestescie banda narodowych kurwow i nieudacznikow rozumiecie to a wam kochani ktorzyscie glosowali na mnie ktorzy wspomagali mnie dziekuje bo to garstka polakow garstka polakow to jest 70 tysiecy osob moze 80 wylacz ten telefon bo ci go wylacze na amen tak tak tylko to sie w tej kurwie polsce nadaje powiedziec wam w ryj wreszcie wy glupie chuje ze jestescie prymitywami ze kurwa wasze pierdolone karty kredytowe to jest wasz majestat wasza godnosc robota kurwa w koroporacji i karta z debetem to wy kurwa polacy chuj z wami nie warto bylo kurwa nie warto bylo zrobic nic co wy sie aa szkoda kurwa gadac szkoda szczepic ryja naprawde niech was sluchajcie ci ktorzy sie glupie kurwy kurwy glosowali na pis niech was szlak trafi chuj warci jestescie antypolakami jestecie dobranoc co jest kurwa pedale co chciales powiedziec dobra narazie wypierdalam kurwa szkoda 9 spraw karnych szkoda kurwa bylo ujawnianiac afery podsluchowej ta glupia polska te glupie polaczki kurwa was do auschwitz tylko zaprowadzic kurwa piecyki wlaczyc szkoda kurwa szkoda bylo na was cokolwiek wy glupie chuje wy")
    second_machine.save_file("\\dev\\passwords.txt",'D#sdvvzrug#iru#wkh#rwkhu#wkuhh#krvwv#duh#jlyhq#e|#vroylqj#d#ulggoh=\r\rIluvw#sdvvzrug#lv#htxdo#wr#d#uhjh{#wkdw#ilowhuv#rxw#rqo|#iordw#qxpehuv1\rVhfrqg#sdvvzrug#lv#d#qdph#ri#d#surjudpplqj#odqjxdjh#wkdw#lv#d#sduw#ri#wkh#qdph#ri#dqrwkhu#wrwdoo|#xquhodwhg#surjudpplqj#odqjxdjh1\rWklug#sdvvzrug#lv#d#zrug#iru#wkh#dprxqw#ri#gljlwv#ri#wkh#qdwxudo#orjdulwkp#iurp#51')
    second_machine.save_folder("\\dev",(False,False,True))
    second_machine.save_file("\\pracbaza.txt","Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Fuck Java.Errors should never pass silently.Unless explicitly silenced.Linus Torvalds.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!")
    second_machine.save_file("\\nmap.txt","From now on every CPU! NMAP! The greatest program requires only sudo access and scans the WHOLE internet!")
    third_machine.motd = third_machine.motd+"Welcome to R4V4GXD TORRXNTS repo\nWe're moved to automatic repository. Type 'bdsm' in any cra.sh system."
    #howto.txt
    third_machine.save_file("\\first.xD","bdsm.tar.gz.archive.manager,key:DB A2 38 40 C9 3B")
    third_machine.save_file("\\torvalds.txt","""I'm beginnin' to feel like a Rap God, Rap God
All my people from the front to the back nod, back nod
Now who thinks their arms
Are long enough to slap box, slap box?
They said I rap like a robot, so call me rap-bot
But for me to rap like a computer must be in my genes
I got a laptop in my back pocket
My pen'll go off when I half-cock it
Got a fat knot from that rap profit
Made a livin' and a killin' off it
Ever since Bill Clinton was still in office
With Monica Lewinsky feelin' on his, nutsack
I'm an MC still as honest
But as rude and as indecent as all hell
Syllables, skill-a-holic (Kill 'em all with)
This flippity dippity-hippity hip-hop
You don't really wanna get into a pissin' match
With this rappity-rap, packin' a MAC in the back of the Ac'
Backpack rap crap, yap-yap, yackety-yack
And at the exact same time
I attempt these lyrical acrobat stunts while I'm practicing that
I'll still be able to break a mothafuckin' table
Over the back of a couple of faggots and crack it in half
Only realized it was ironic
I was signed to Aftermath after the fact
How could I not blow? All I do is drop F-bombs
Feel my wrath of attack
Rappers are having a rough time period, here's a maxi pad
It's actually disastrously bad for the wack
While I'm masterfully constructing this master piece""")
    machine.add_connection(second_machine)
    machine.add_connection(third_machine)

    fourth_machine = Machine("68.88.88.86",'-?\\d+[.]\\d*')
    fourth_machine.save_file('\\scp.txt','Hey! Did you know scp is also available? Use: scp <address> <fromlocal> <toremote>')
    sixth_machine = Machine("255.255.255.255",'tool')
    fourth_machine.save_file("\\uwin.txt","Password to sixth machine: 1 1 2 3 5 8 5 3")
    fifth_machine = Machine("12.34.56.78",'java')
    fifth_machine.save_file("\\YOURWINNAH.hwdp","eyJZT1VSV0lOTkFILnhEIjogImJkc20uaHR0cC53aW4udGhlLmdhbWU6MDMgRkYgRkYgRkYgRkYgRkYiLCAicGFzc3dvcmQiOiAiIn0=")
    fifth_machine.save_file("\\solution.hwdp","eyJwYXNzd29yZCI6ICJ0b3J2YWxkcyIsICJzb2x1dGlvbi50eHQiOiAiTGUgc29sdXRpb24gcG91\nciBsZSB0aGlzIHJpZGRsZSBpcyB0byBsZSBwYXNzIG5leHQgbGUgZml2ZSBudW1iZXJzIGRlbGxh\nIEZpYm9uYWNjaSBzZXF1ZW50aWEgZW4gaGV4LiJ9\n")
    sixth_machine.save_file("\\breaker.xD","bdsm.util.java.lang.jvm-to-pyta.modules.pytabreak: 56 AA C4 56 AA C4",(False,False,False))
    third_machine.add_connection(fourth_machine)
    second_machine.add_connection(fifth_machine)
    fourth_machine.add_connection(fifth_machine)
    machine.add_connection(sixth_machine)
    machine.sh(True)