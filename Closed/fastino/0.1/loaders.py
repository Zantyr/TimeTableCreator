import re

#proto-dev constructs devices - needs constructors to be initialized
class ProtoDev(object):
    def __init__(self,obj_type,constructors):
        self.obj_type = obj_type
        self.constructors = constructors
    def construct(self):
        try:
            return self.constructors[self.obj_type](self)
        except TypeError:
            try:
                return self.constructors[0](self)
            except TypeError:
                return self.constructors(self)

#this code spawns PROTO_DEVS for all objects in the file
#proto-devs will the .construct into objects into the appropiate lists
def load_dev(dev_attrs,constructors,files):
    proto_devs = []
    for fi in files:
        with open(fi,'r') as f:
            for line in f:
                try:
                    attribute,value = map(lambda x: x.strip(),map(lambda x:re.match("(.*)=(.*)",line).group(x),[1,2]))
                except: #IndexError, AttributeError:
                    if line[0]!="#" and line!="":
                        try:
                            comm,value = map(lambda x:re.match("([^ \t]*) ([^ \t]*)",line).group(x),[1,2])
                            if comm == "NEW" or comm=="DEFINE":
                                last_object = ProtoDev(value,constructors)
                                proto_devs.append(last_object) #czy tutaj zostanie podane przez referencje?
                        except IndexError, AttributeError:
                            pass #nieodpowiedni format kodu
                    continue
                for var in dev_attrs:
                    if attribute==var:
                        try:
                            setattr(last_object,attribute,value)
                        except:
                            pass #nie ma obiektu
                else:
                    pass #no such attribute
    return proto_devs

#this code creates definitions of various lists in the file
def load_list(filename):
    d = []
    with open(filename,"r") as f:
        for line in f:
            if line.strip() != '':
                d.append(line.strip())
    return d 
