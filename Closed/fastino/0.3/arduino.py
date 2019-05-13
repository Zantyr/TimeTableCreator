#main constructing class
#interfaces methods to add/edit devices
#requires resource manager to effectively manage what is in the device and detect overflows of InoResources


#needs a properly build device attachment process, that registers resources and assigns them

#consider differentiating devices and the devicetypes, as they are one type of objects right now

import os
import re
import exce

import constants as C
import loaders
import properties as P
import res
import devs


DEV_TYPES = loaders.dev_loader(devs.Device)
DEV_TYPES = map(lambda x:(x.name,x),DEV_TYPES)
DEV_TYPES = dict(DEV_TYPES)

#this is main control of the Arduino board, an Application core
#it has to have added all the devices and building blocks and connect is to a steady stream of data
#needs to manage relationships between input and output, because it obviously needs it
class Arduino(object):
    def __init__ (self,dev_type="uno"):
        self.resource_manager = res.InoResources(dev_type)
        self.sensors = []
        self.processors = []
        self.outputs = []
        self.controls = []
        self.rate = 0.05
    def add(self,objtype,inps=[]):
        if objtype in DEV_TYPES.keys():
            dev = DEV_TYPES[objtype]
            copy = dev._class()
            outs = copy.load(inps)
            copy.load_res(self.resource_manager)
            if copy.type == "sensor": self.sensors.append(copy)
            elif copy.type == "processor": self.processors.append(copy)
            elif copy.type == "output": self.outputs.append(copy)
            elif copy.type == "controllers": self.controllers.append(copy)
            else: raise exce.NoSuchDeviceTypeException
            return outs
        else:
            raise exce.NoSuchDeviceException
    def best_indent(self,text):
        lines = text.split('\n')
        lines = map(lambda x: x.strip(),lines)
        indent = 0
        copy = []
        for i in lines:
            n = indent*'    '+i
            copy.append(n)
            indent += i.count('{')
            indent -= i.count('}')
        return '\n'.join(copy)
    def build(self):
        headers = ""
        for i in self.sensors+self.outputs+self.controls:
            if i.get_headers(): headers += i.get_headers() + "\n"
        setup = ""
        for i in self.sensors+self.processors+self.outputs+self.controls:
            if i.get_setup(): setup += i.get_setup() + "\n"
        fndefs = ""
        for i in self.sensors+self.processors+self.outputs+self.controls:
            if i.get_fndefs(): fndefs += i.get_fndefs() + "\n"
        loop = ""
        for i in self.sensors+self.processors+self.outputs+self.controls:
            if i.get_loop(): loop += i.get_loop() + "\n"
        self.libs = []
        for i in self.sensors+self.processors+self.outputs+self.controls:
            self.libs += i.get_libs()
        self.code = "".join([headers,fndefs,"\nvoid setup(){\n",setup,"}\n\nvoid loop(){\n",loop,"sleep("+str(int(self.rate*1000))+");\n}"])
        return self.best_indent(self.code)
    def compile(self):
        os.system("mkdir tmpino")
        os.chdir("tmpino")
        os.system("ino init")
        os.system("")
        for lib in libs:
            os.system("cp ../libs/" + self.libs + " src/" + self.libs)
        with open("src/sketch.ino","w") as f:
            f.write(self.code)
        os.system("ino build")
        os.system("ino upload")
        os.chdir("..")
        os.system("rm -r tmpino")
        #return the pin-up schematics
