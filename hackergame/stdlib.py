from __future__ import print_function
from __future__ import division

#JEBANA GRA DLA BRATA
from time import sleep
try: input=raw_input
except NameError: pass
from core import CoreMachine
from pyta import pyta

#manual
MAN={'pyta':"""\nPyta programming language\nUnstable and experimental\nFeatures may not work correctly\n\nOverall syntax:\n(a b c ...) => a(b,c,...)\n\nSyntax tips:\n(' x)     - return x unevaluated\n(# x y)   - set uneval x to y\n(#! x y)  - set evalled x to y\n(! x)     - execute list x, ret last\n(!: ...)  - execute unpacked list\n(? x y)   - if x execute y\n(? x y z) - if x then y else z\n\nCommands:\n'&': sum the arguments\n'*': multiply the arguments\n'-': subtract\n'/': division\n'/-': modulo\n':': print (accepts :' as a parameter to print strings)\n'@': access the nth element of a list\n'@#': append argument to list\n'#@': x[y]=z\n'--': negate\n'**': power\n'!**': logarithm\n'#-#': range(may not work)\n'@..': list from args\n'$$$': load file\n'!?': get input :' for strings\n'###': save file\n""",

     'man':"""This is GNU manual page\n\nYou may want to find some help there.\njust type 'man <topic>'\nGood luck\n\nUseful commands: ls, cd, dog, pyta, ssh, lgbt, chmod, mkdir, rm""",

     'ls':"Log out. Seriously.\nThis actually shows only the current folder.",

     'cd':"This varies from normal cd: there's no ..",

     "lgbt":'Low Grade Budget Text-editor\nUnlike vim has only command mode\n+:text appends text\n+:number inserts a line\n-:number removes a line\n?:number shows a scope\n? shows whole document\nnumber:text replaces the given line with the text\nquit - quits ofc',

     'dog':'This is the plain old cat. Copyleft, all rights reversed.','nmap':'This actually requires no parameters. Instead, it needs root access.',

     'scp':'One-way copy through ssh\nusage:scp host localsource remotetarget\nlocally uses $PWD','chmod':'This chmod has cow super-powers',

     'bdsm':'BADLY DESIGNED SCRIPTING MACHINE\n\nBudget version of apt-get\nbdsm <name> either runs a script or installs it if key is available',

     'mkdir':'www.google.com',

     'rm':'Removes an element, either file or folder. Doesn\'t do it recursively.'}

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

class Machine(CoreMachine):
    """
    Has filesystem (root), shows sh(...) that acts as a shell, has also network_env
    """
    def __init__(self,ip_address,password,iso=None):
        super(Machine,self).__init__(ip_address,password,iso)
        
        self.calls = {'ls':self.__ls,
                      'man':self.__man,
                      'help':self.__help,
                      'cd':self.__cd,
                      'pyta':self.__pyta,
                      'ssh':self.__ssh,
                      'scp':self.__scp,
                      'dog':self.__dog,
                      'lgbt':self.__lgbt,
                      'bdsm':self.__bdsm,
                      'nmap':self.__nmap,
                      'chmod':self.__chmod,
                      'mkdir':self.__mkdir,
                      'rm':self.__rm}
        self.motd = "Hello in cra.sh OS\nversion 1.0.3 build nightly\nMachine: "+self.ip_address+"\n\n"
    def __cd(self,*args):
        if not args:
            self.env['$PWD']="\\"
        else:
            try:
                assert(self.get_file(self.__pwd(args[0])).perms()[2] == 'd')
            except KeyError:
                print("No such folder")
                return
            except AssertionError:
                print("Is a file")
                return
            try:
                assert(self.get_file(self.__pwd(args[0])).perms()[0] == 'r')
                self.env["$PWD"]=self.__pwd(args[0])
            except AssertionError:
                print("No read permissions to enter this folder")
    def __chmod(self,*args):
        if not args: 
            print("Pass actual file")
            return
        pw = input("Root access is needed: ")
        if pw==self.sudo_password:
            self.get_file(self.__pwd(args[0])).unlock()
        else:
            sleep(2)
            print("Incorrect password")
    def __ls(self,*args):
        try:
            file = self.get_file(self.env["$PWD"]+(("\\"+args[0]) if args else ""))
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
            file = self.get_file(self.__pwd(args[0]))
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
                    file = self.get_file(self.__pwd(args[1]))
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
            file = self.get_file(self.__pwd(args[0]))
            if(file.perms()[0]=='r'):print(file.content)
            else:print("Cannot read this file")
        except KeyError:
            print("No such file")
    def __lgbt(self,*args):
        if not args:
            buffer = ""
        else:
            try:
                file = self.get_file(self.__pwd(args[0]))
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
        self.save_file(self.__pwd(args[0]),buffer)
    def __bdsm(self,*args):
        if not args:
            print("BDSM Fataler Fehler: keine Skript gewahlt.")
            return
        try:
            func = self.env[args[0]]
        except KeyError:
            try:
                key = self.get_file(self.__pwd(args[0])).content
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
        self.save_folder(self.__pwd(args[0]))
    def __rm(self,*args):
        if not args:
            print("Give an input file")
            return
        self.delete(self.__pwd(args[0]))
    def __help(self,*args):
        print("No such command, man")
    def __pwd(self,name):
        return self.env["$PWD"]+("\\" if self.env["$PWD"]!="\\" else "")+name