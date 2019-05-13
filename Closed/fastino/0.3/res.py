'''
Przy ladowaniu programu, wczytaj wszystkie zasoby do urzadzenia. (w obiekcie Arduino). Arduino tworzac urzadzenie sprawdza wymagania przez wywolanie klasy device atrybut .reqs podaje do Managera urzadzen (Obiekt InoResources) i metoda obiektu sprawdza, czy sa dostepne zasoby. Jesli nie, sprawdza, czy moze poprzesuwac istniejace zasoby, aby zwolnic zasoby potrzebne do nowego urzadzenia. Jesli tak, robi to i wypluwa z siebie zasoby, rezerwujac je u siebie. Jesli nie, blad, terminacja (NoFreeResources). Zasoby sa przydzielane w kolejnosci od gory, (powinno byc priorytetem dla zasobow z najmniejsza iloscia flag, ale nie jest). Istnieje jeszcze mozliwosc robienia wirtualnych portow (Software serial, Multi I2C). Klasa InoResources moze dopuszczac tworzenie logicznych zasobow. Flaga multi przydziela adresy.(tego tez nie ma)

Klasa resources ma funkcje inicjalizacyjne i funkcje odczytu/zapisu.
'''

import exce
import constants as C
import loaders

#returns %resname_init% %resname_read% %resname_write%
#i2c and spi to be done
class Resource(object):
    def __init__(self,name,flags,dependencies=[],write="",read=""):
        self.name = name
        self.flags = flags
        self.dependencies = dependencies #moga byc nazwy lub flagi (dla wirtuali)
    def pass_resources(self,res):
        pass
    def initialize(self,mode="read"):
        if "digital" in flags:
            return "pinMode("+self.name+","+("OUTPUT" if mode=="write" else "INPUT")+");"
        elif "serial" in flags:
            return self.name+" = Serial.begin(9600);"
    def read(self):
        if "analog" in flags:
            return "analogRead("+self.name+");"
        elif "digital" in flags:
            return "digitalRead("+self.name+");"
        elif "serial" in flags:
            return self.name+".read();"
    def write(self,varname):
        if "digital" in flags:
            return "digitalWrite("+self.name+","+varname+"?HIGH:LOW);"
        elif "serial" in flags:
            return self.name+".print("+varname+");"

proto_models = loaders.xml_models()
INO_MODELS = {}
for i in proto_models:
    ress = []
    for proto_res in proto_models[i]:
        ress.append(Resource(*proto_res))
    INO_MODELS[i]=ress

class InoResources(object):
    '''
    This class is a resource manager for Arduino device. 
    '''
    def __init__(self,dev_type):
        self.resources = INO_MODELS[dev_type]
        self.availability = {}
        for i in self.resources:
            self.availability[i.name] = (False,None)
        self.virtual_constructors = {} #to-be-done
    def request_resources(self,to_what,resources):
        '''
        Reserves resources that are to be used. Uses the algorithm specified in the header of this module. Calls self recursively for dependencies, however dependencies are not likely nested.
        '''
        resources_returned = []
        for requested in resources:
            for resource in self.resources:
                if requested in resource.flags or resource.name == requested:
                    if self.availability[resource.name][0] == False:
                        self.availability[resource.name] = (requested,to_what)
                        #self.request_resources(resource.dependencies,resource)
                        resources_returned.append(resource)
                        break
            else:
                for resource in self.resources:
                    if requested in resource.flags or resource.name == requested:
                        self.unfree(resource)
                        self.availability[resource.name] = (requested,to_what)
                        #self.request_resources(resource.dependencies,resource)
                        resources_returned.append(resource)
                        break
                else:
                    for cons in self.virtual_constructors:
                        if cons.resource_constructed==requested:
                            res = cons()
                            self.resources.append(res)
                            self.availability[res.name] = (requested,to_what)
                            #self.request_resources(res.dependencies,res)
                            resources_returned.append(res)
                            break
                    else:
                        raise exce.ResourceUnavailable
        to_what.pass_resources(resources_returned)
    def unfree(self,freeable):
        '''
        Unloads the resources, that are to be moved. Internal function.
        '''
        self.availability[freeable.name] == (True,None)
        for i in freeable.dependencies:
            self.unfree(i)
