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
from exceptions import *
import constants as C
import loaders
import properties

#this is a parent class for all devices, contains common building functions
class Device(object):
    def get_headers(self):
        return self.headers
    def set_headers(self):
        self.headers = HEADERS[self.devicetype][self.devicename]
    def get_setup(self,devices):
        pass
    def get_fndefs(self,devices):
        pass
    def get_loop(self):
        pass
    def get_libs(self):
        pass

#sensor class has to initialize it, initialize a proper variable for storage, reserving resources on the board
#it has to write a function that reads the data from the device, converts it and returns in a pregiven form (e.g. int _Temperature1)
class Sensor(Device):
    def __init__(self,name,objecttype,**kwargs):
        self.name = name
        self.sensortype = objecttype
        self.address = kwargs[address] if "address" in kwargs.keys() else None
        self.prop_type = None
        self.measured_property = PROPERTIES.new(self.name,prop_type)
    def get_free_adresses(self, usedadresses):
        pass

#############################CONSTRUCTOR FOR SENSORS

#############################SPAWN SENSORS FROM PROTO_DEVS

#############################CONTROLLER DEFINITION

#############################CONTROLLER COSNTRUCTOR

#############################CONTROLLER SPAWNING

#############################OUTPUT DEFINITION

#############################OUTPUT CONSTRUCTOR

#############################OUTPUT SPAWNING

#############################processor DEFINITION

#############################proc COSNTRUCTOR

#############################proc SPAWNING

#this is main control of the Arduino board, an Application core
#it has to have added all the devices and building blocks and connect is to a steady stream of data
#needs to manage relationships between input and output, because it obviously needs it
class Arduino(object):
    #this has to be imported
    SENSOR_TYPES = {}
    CONTROLLER_TYPES = {}
    OUTPUT_TYPES = {}
    PROCESSOR_TYPES = {}
    def __init__ (self):
        self.sensors = []
        self.processors = []
        self.outputs = []
        self.controls = []
        self.rate = 0.05
        self.reserved_resources = []
    def add(self,objtype):
        if objtype in SENSOR_TYPES.keys():
            self.add_sensor(objtype)
        elif objtype in CONTROLLER_TYPES.keys():
            self.add_controller(objtype)
        elif objtype in OUTPUT_TYPES.keys():
            self.add_output(objtype)
        elif objtype in PROCESSOR_TYPES.keys():
            self.add_processor(objtype)
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
            setup += i.get_setup(self.sensors+self.processors+self.outputs+self.controls)
        fndefs = ""
        for i in self.sensors+self.processors+self.outputs+self.controls:
            fndefs += i.get_fndefs(self.sensors+self.processors+self.outputs+self.controls)
        loop = ""
        for i in self.sensors+self.processors+self.outputs+self.controls:
            fndefs += i.get_loop(self.sensors+self.processors+self.outputs+self.controls)
        libs = []
        for i in self.sensors+self.processors+self.outputs+self.controls:
            libs += i.get_libs(self.sensors+self.processors+self.outputs+self.controls)
        buildoutput = "\n".join([headers,fndefs,"void setup(){",setup,"}\nvoid loop(){",loop,"sleep("+str(int(self.rate*1000))+");}"])
        os.system("mkdir tmpino")
        os.chdir("tmpino")
        os.system("ino init")
        os.system("")
        for lib in libs:
            os.system("cp ../libs/" + lib + " src/" + lib)
        with open("src/sketch.ino","w") as f:
            f.write(buildoutput)
        os.system("ino build")
        os.system("ino upload")
        os.chdir("..")
        os.system("rm -r tmpino")
        #return the pin-up schematics

#this function runs a wizard that easily creates a proper device by asking from prompt for needed devices, and other building blocks
#can also give help and create a device from file, can store, push and pull from server different schematics and libs
def arduino_device_creator():
    dev = Arduino()
    dev.build()

if __name__ == "__main__":
    arduino_device_creator()


    '''


Full abstract of functions:
%return_type% %dev_name%_%dev_type%_%dev_function% (%dev_args.build_text%)
{
    %calculation code%;
    return %return_variable%;
}

Patterned abstract (already in files):
int %dev_name%_PID_process(int input_signal)
{
    int P = 10;
    int output_signal;
    input_signal = %type_cast_function%(input_signal);
    output_signal = P*input_signal;
    return output_signal;
}

Constructed code:
int generic_PID_PID_process(int input_signal)
{
    int P = 100;
    int output_signal;
    input_signal = temperature_m40_60_int16_to_temperature_0_20_int8(input_signal);
    output_signal = P*input_signal;
    return output_signal;
}
*
    '''