from __future__ import print_function
from __future__ import division
from time import sleep
try: input=raw_input
except NameError: pass

"""
This module implement basic
"""

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

class CoreMachine(object):
    """
    Has filesystem (root), shows sh(...) that acts as a shell, has also network_env
    """
    def __init__(self,ip_address,password,iso=None):
        if iso:
            self.root = Root(iso)
        else:
            self.root = Root()
        self.env = {"$PWD":'\\'}
        self.calls = {}
        self.sudo_password = password
        self.ip_address = ip_address
        self.network={self.ip_address:self}
        self.motd = "Hello in cra.sh OS\nversion 1.0.0 stable\nMachine: "+self.ip_address
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
    def save_file(self,abs_name,content="",permissions=(True,True,False)):
        self.root.memory[abs_name] = File(content,permissions)
    def save_folder(self,abs_name,permissions=(True,True,True)):
        self.root.memory[abs_name] = Folder(abs_name,self.root,permissions)
    def add_connection(self,machine):
        self.network[machine.ip_address] = machine
        machine.network[self.ip_address] = self