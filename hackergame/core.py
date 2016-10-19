from __future__ import print_function
from __future__ import division
import readline
from time import sleep
try: input=raw_input
except NameError: pass

"""
This module implement basic
"""

class File(object):
    def __init__(self,content="",perms=(True,True,False)):
        self.content=content
        self._perms = list(perms)
    def perms(self):
        return ("r" if self._perms[0] else "-")+("w" if self._perms[1] else "-")+("d" if self._perms[2] else "-")
    def unlock(self):
        self._perms[0] = True
        self._perms[1] = True
    def to_dict(self):
        return {'content':self.content,'perms':self._perms}
    @classmethod
    def from_dict(cls,node):
        obj = File(node['content'],node['perms'])
        return obj

class Folder(File):
    def __init__(self,name,root,perms=(True,True,True)):
        self.name = name
        self.root = root
        self._perms = list(perms)
    def get_files(self):
        return self.root.get_files(self.name)
    def to_dict(self):
        return {'perms':self._perms,'abs_name':self.name}
    @classmethod
    def from_dict(cls,node,root):
        obj = Folder(node['abs_name'],root,node['perms'])
        return obj

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
    def reconstruct(self,dict):
        for key in dict:
            if dict[key]['perms'][2]==False:
                self.memory[key] = File.from_dict(dict[key])
            else:
                self.memory[key] = Folder.from_dict(dict[key],self)

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
    def remove_connection(self,name):
        self.network[name].network.pop(self.ip_address)
        self.network.pop(name)
    def get_file(self,abs_name):
        return self.root.get_file(abs_name)
    def get_folder(self,abs_name):
        return self.root.get_files(abs_name)
    def delete(self,abs_name):
        self.root.memory.pop(abs_name)
    def get_env(self,name):
        return self.env[name]
    def set_env(self,name,value):
        self.env[name]=value
    def to_dict(self):
        node = {'machine_type': self.__class__.__name__,'sudo_password':self.sudo_password,'ip_address':self.ip_address,
                'network':[x for x in self.network],'motd':self.motd,'bye':self.bye,'root':{key:self.root.memory[key].to_dict() for key in self.root.memory},'env':self.env}
        return node
    @classmethod
    def from_dict(cls,node):
        obj = cls(node['ip_address'],node['sudo_password'])
        obj.network = node['network']
        obj.motd = node['motd']
        obj.bye=  node['bye']
        obj.root.reconstruct(node['root'])
        obj.env = node['env']
        return obj