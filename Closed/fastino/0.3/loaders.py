#the file contains various methods to store objects needed in program, so they can be modified

import constants as C
import os
import re
import xml.etree.ElementTree as ET

def dev_loader(Device):
    files = []
    for i,j,k in os.walk(C.DEV_PATH):
        for item in k:
            files.append(i+"/"+item)
    evalable = ["inputs","outputs","resources","libs"]
    dev_list = []
    constrs = {"device":Device}
    for f in files:
        dev_list += (xml_loader(f,constrs))
    new_list = []
    for i in dev_list:
        for j in evalable:
            setattr(i,j,eval(getattr(i,j)))
        new_list.append(i)
    return new_list

#this creates lists from XML
def xml_models():
    models = []
    files = []
    for i,j,k in os.walk(C.INO_PATH):
        for item in k:
            files.append(i+"/"+item)
    for file in files:
        models += xml_loader(file,{})
    models = map(lambda x: (x.name,x.__dict__),models)
    newmodels = {}
    for name,dic in models:
        del dic['name']
        modellist = []
        for i in dic:
            content = dic[i]
            if i[0]=="_":i = i[1:]
            resource = [i]+list(eval(content))
            modellist.append(resource)
        newmodels[name] = modellist
    return newmodels

#load objects from XML
def xml_loader(file,constructors):
    with open(file,"r") as f:
        string = f.read()
    root = ET.fromstring(string)
    items = []
    for child in root:
        try:
            item = constructors[child.tag]()
        except:
            class Empty(object):
                pass
            item = Empty()
        for attr in child.attrib:
            setattr(item,attr,child.attrib[attr])
        for attribute in child:
            setattr(item,attribute.tag,(attribute.text if attribute.text else ""))
        items.append(item)
    return items

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
