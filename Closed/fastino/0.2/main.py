#QVICKSILVER PID
#for fast Arduino measurement/regulation modules

#subgoal: build properties calculator with creation of conversions

#######
#Build a builder for analog input and serial output of data

#process of doing:
#   finish the sensor class
#       have resources grouped to classes, and may require more than one of given resource
#   finish the processor class
#   finish the controller and output classes - MVP
#   add all the remaining structures, imports etc
#   create a wizard for building the bricks

#import public libraries
import os
import re

#import custom libraries
from exce import *
import constants as C
import loaders
import properties as P
import res

#this is a parent class for all devices, contains common building functions
class Device(object):
    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.ress = []
        self.headers = ""
        self.setup = ""
        self.fndefs = ""
        self.loop = ""
        self.libs = []
    def load(self,inps,outs):
        if(self.inputs == len(inps)):self.inputs = inps
        else: raise BaseException
        if(self.outputs == len(outs)):self.outputs = outs
        else: raise BaseException
        return self
    def subst(self,string):
        self.replacements = {"%dev_name%":self.name,
#to-do        "%res_0%":self.resources[0].name,
        "%in_0%":self.inputs[0].name,
#        "%out_0%":self.outputs[0].name,
        "%dev_var%":self.name+"_var_",
        r"\p":r"%",
        r"\s":"\\"}
        for r in self.replacements:
            string = string.replace(r,self.replacements[r])
        return string
    def get_headers(self):
        return self.subst(self.headers)
    def get_setup(self):
        return self.subst(self.setup)
    def get_fndefs(self):
        return self.subst(self.fndefs)
    def get_loop(self):
        return self.subst(self.loop)
    def get_libs(self):
        return self.libs

DEV_TYPES = loaders.dev_loader(["incs/diode.dev"],Device)
DEV_TYPES = map(lambda x:(x.name,x),DEV_TYPES)
DEV_TYPES = dict(DEV_TYPES)

#this is main control of the Arduino board, an Application core
#it has to have added all the devices and building blocks and connect is to a steady stream of data
#needs to manage relationships between input and output, because it obviously needs it
class Arduino(object):
    #this has to be imported
    SENSOR_TYPES = {}
    CONTROLLER_TYPES = {}
    OUTPUT_TYPES = {}
    PROCESSOR_TYPES = {}
    def __init__ (self,dev_type="uno"):
        self.resource_manager = res.InoResources(dev_type)
        self.sensors = []
        self.processors = []
        self.outputs = []
        self.controls = []
        self.rate = 0.05
    def add(self,objtype,inps=[],outs=[]):
        if objtype in DEV_TYPES.keys():
            dev = DEV_TYPES[objtype]
            dev.load(inps,outs)
            if dev.type == "sensor": self.sensors.append(dev)
            elif dev.type == "processor": self.processors.append(dev)
            elif dev.type == "output": self.outputs.append(dev)
            elif dev.type == "controllers": self.controllers.append(dev)
            else: raise NoSuchDeviceTypeException
        else:
            raise NoSuchDeviceException
    def add_sensor(self, objecttype):
        #check for conflicts with addresses
        self.sensors.append(Sensor(name,objecttype))
    def add_controller(self, objecttype):
        #check for conflicts with addresses
        self.controls.append(Sensor(name,objecttype))
    def add_output(self, objecttype):
        #check for conflicts with addresses
        self.output.append(Sensor(name,objecttype))
    def add_processor(self, objecttype):
        self.processors.append(Sensor(name,objecttype))
    def build(self):
        headers = ""
        for i in self.sensors+self.outputs+self.controls:
            headers += i.get_headers()
        setup = ""
        for i in self.sensors+self.processors+self.outputs+self.controls:
            setup += i.get_setup()
        fndefs = ""
        for i in self.sensors+self.processors+self.outputs+self.controls:
            fndefs += i.get_fndefs()
        loop = ""
        for i in self.sensors+self.processors+self.outputs+self.controls:
            loop += i.get_loop()
        self.libs = []
        for i in self.sensors+self.processors+self.outputs+self.controls:
            self.libs += i.get_libs()
        self.code = "\n".join([headers,fndefs,"void setup(){",setup,"}\n\nvoid loop(){",loop,"sleep("+str(int(self.rate*1000))+");\n}"])
        return self.code
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

#this function runs a wizard that easily creates a proper device by asking from prompt for needed devices, and other building blocks
#can also give help and create a device from file, can store, push and pull from server different schematics and libs
def arduino_device_creator():
    dev = Arduino()
    dev.add("diode_output",[P.PROPERTIES.new("test_out","temp0-255")]) #add output
    print dev.build()

if __name__ == "__main__":
    arduino_device_creator()