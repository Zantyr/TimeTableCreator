import exce
import constants as C
import loaders

#property declares a variable of a given type and governs how variables are converted and what kind of data it is
#it contains data about units, names, modules can convert their internal data to different properties and use different kinds of those
class Property(object):
    _AVAILABLE_UNITS = loaders.load_list(C.UNITS_PATH)
    _AVAILABLE_SCALES = loaders.load_list(C.SCALES_PATH)
    _C_TYPES = eval('\n'.join(loaders.load_list(C.DATA_TYPES_PATH)))
    _AVAILABLE_DATA_TYPES = _C_TYPES.keys()
    def __init__(self,name,unit,scale=(0,100),scale_type=None,storage_type=None):
        self.name = name
        self.unit = self.set_unit(unit)
        self.scale = scale
        self.scale_type = self.set_scale_type(scale_type)
        self.storage_type = self.set_storage_type(storage_type)
    def set_unit(self, unitname):
        if unitname in self._AVAILABLE_UNITS:
            return unitname
        else:
            raise exceptions.NoSuchUnitException
    def set_scale_type(self, scale_type):
        if scale_type is not None:
            if scale_type in self._AVAILABLE_SCALES:
                return scale_type
            else:
                raise exceptions.NoSuchScaleException
        else:
            return _AVAILABLE_SCALES[0]
    def set_storage_type(self, storage_type):
        if storage_type is not None:
            if storage_type in self._AVAILABLE_DATA_TYPES:
                return storage_type
            else:
                raise exceptions.NoSuchDataTypeException
        else:
            return _AVAILABLE_DATA_TYPES[0]
    def get_C_type(self):
        return self._C_TYPES[self.storage_type]

#this is a global repository for all variables used through the measurement process
class Properties(object):
    _PROP_TYPES = {}
    def __init__(self):
        self.converters = {"linear-16-unsigned-integer:linear-16-unsigned-integer":self.linear16unsignedinteger_linear16unsignedinteger,"linear-16int:linear-16int":self.linear16unsignedinteger_linear16unsignedinteger}
        self.properties = []
    def add(self,prop):
        self.properties.append(prop)
    def new(self, dev_name,prop_type):
        prop_names = map(lambda x: x.name,self.properties)
        for i in xrange(100):
            if "_".join([dev_name,prop_type,str(i)]) not in prop_names:
                found_new_name = "_".join([dev_name,prop_type.replace("-","_"),str(i)])
                break
        try:
            prop = Property(found_new_name,*self._PROP_TYPES[prop_type])
        except KeyError:
            raise exce.NoSuchProperty
        self.properties.append(prop)
        return prop
    def convert(self,prop1,prop2):
        conversion_name = prop1.scale_type+"-"+prop1.storage_type+":"+prop2.scale_type+"-"+prop2.storage_type
        return self.converters[conversion_name](prop1,prop2)
    def linear16unsignedinteger_linear16unsignedinteger(self,A_prop,B_prop):
        depth = 2**16
        A_scale,B_scale = A_prop.scale,B_prop.scale
        zero_point = B_scale[0] - A_scale[0]
        proportional_ratio = (float(B_scale[1] - B_scale[0])/(depth-1))/(float(A_scale[1] - A_scale[0])/(depth-1))
        return B_prop.get_C_type()+" "+B_prop.name+" = (" + B_prop.get_C_type() + ") ("+str(proportional_ratio)+"*"+A_prop.name+("+" if zero_point>=0 else "")+str(zero_point)+");"
    def dump(self):
        return self.properties

#this adds types of properties to Properties
class PropertyType(object):
    def __init__(self, proto_dev):
        self.name = proto_dev.name
        self.tuple = proto_dev.unit,map(lambda x: float(x),proto_dev.scale.strip("() ").split(",")),proto_dev.scale_type,proto_dev.storage_type

proto = loaders.load_dev(['name','unit','scale','scale_type','storage_type'],[PropertyType],[C.PROPERTIES_PATH])
for prop in map(lambda x: x.construct(),proto):
    Properties._PROP_TYPES[prop.name] = prop.tuple

PROPERTIES = Properties()

#############################DEFINE PROPERTIES CONVERTER CONSTRUCTOR

#############################SPAWN CONVERTERS INTO PROPERTIES