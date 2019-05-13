#generic item constructor
#to be used in fastino and be reused anywhere else
import re

FILES = []
DEV_ATTRS = []
PROTO_DEVS = []
CONSTRUCTORS = {}

#proto-dev constructs devices - needs constructors to be initialized
class ProtoDev(object):
    def __init__(self,obj_type):
        self.obj_type = obj_type
        self.constructors = CONSTRUCTORS
    def construct(self):
        self.constructors[self.obj_type](self)

#this code spawns PROTO_DEVS for all objects in the file
#proto-devs will the .construct into objects into the appropiate lists
def load_dev():
    for fi in FILES:
        with open(fi,'r') as f:
            for line in f:
                try:
                    attribute,value = map(lambda x: x.strip(),map(lambda x:re.match("(.*)=(.*)",line).group(x),[1,2]))
                except IndexError, AttributeError:
                    if line[0]!="#" and line!="":
                        try:
                            comm,value = map(lambda x:re.match("([^ \t]*) ([^ \t]*)",line).group(x),[1,2])
                            if comm == "NEW" or comm=="DEFINE":
                                last_object = ProtoDev(value)
                                PROTO_DEVS.append(last_object) #czy tutaj zostanie podane przez referencje?
                        except IndexError, AttributeError:
                            pass #nieodpowiedni format kodu
                    continue
                for var in DEV_ATTRS:
                    if attribute==var:
                        try:
                            setattr(last_object,attribute,value)
                        except:
                            pass #nie ma obiektu
                else:
                    pass #no such attribute
