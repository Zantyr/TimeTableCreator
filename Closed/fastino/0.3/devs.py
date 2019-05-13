#this class, when executed and fed with resources and properties has to produce an eligible C code to be inserted

#inputs and outputs has to be created based on the numbers of them; appropiate conversions have to be applied
#inouts are pushed from other devs and used to store local vars containing scaled inputs
#outputs are created by the device according to recipes in <outputs> tag
#resources are inserted into the code simply, they publish a code for most read/write/setup func and you use it

#self.replacements are generated dynamically during the self.subst, because of variable number of ress, ins, outs

import properties as P

#this is a parent class for all devices, contains common building functions
class Device(object):
    def __init__(self,*args):
        self.inputs = []
        self.outputs = []
        self.resources=[]
        self.headers = ""
        self.setup = ""
        self.fndefs = ""
        self.loop = ""
        self.replacements = None
        self.libs = []
    def _class(self):
        class c:
            def __init__(self,i,o,r,h,s,f,l,rp,li,na,ty):
                self.inputs=i
                self.outputs=o
                self.resources=r
                self.headers=h
                self.setup =s
                self.fndefs =f
                self.loop =l
                self.replacements = rp
                self.libs = li
                self.name = na
                self.type = ty
            def pass_resources(self,res):
                self.resources = res
            def load(self,inps):
                self.converters = []
                newinputs = []
                for i in self.inputs:
                    newinputs.append(P.PROPERTIES.new(self.name,i))
                self.inputs = newinputs
                for i,j in zip(inps,self.inputs):
                    self.converters.append(P.PROPERTIES.convert(i,j))
                newoutputs = []
                for i in self.outputs:
                    newoutputs.append(P.PROPERTIES.new(self.name,i))
                self.outputs = newoutputs
                return self.outputs
            def load_res(self,res_manager):
                res_manager.request_resources(self,self.resources)
            def subst(self,string):
                if self.replacements is None:
                    self.replacements = {"%dev_name%":self.name,
                    "%dev_var%":self.name+"_var_"}
                    for n,i in enumerate(self.resources):
                        self.replacements["%res_"+str(n)+"%"] = i.name
                        #self.replacements["%res_"+str(n)+"_setup%"] = i.setup
                        #self.replacements["%res_"+str(n)+"_read%"] = i.read
                        #self.replacements["%res_"+str(n)+"_write%"] = i.write
                    for n,i in enumerate(self.inputs):
                        self.replacements["%in_"+str(n)+"%"] = i.name
                        self.replacements["%in_"+str(n)+"_declare%"] = i.get_C_type() + " " + i.name + ";"
                    for n,i in enumerate(self.outputs):
                        self.replacements["%out_"+str(n)+"%"] = i.name
                        self.replacements["%out_"+str(n)+"_declare%"] = i.get_C_type() + " " + i.name + ";"
                    if self.converters:
                        self.replacements["%conv_0%"] = self.converters[0]
                    self.replacements[r"\p"] = r"%"
                    self.replacements[r"\n"] = "\n"
                    self.replacements[r"\s"] = "\\"
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
        o = c(self.inputs,self.outputs,self.resources,self.headers,self.setup,self.fndefs,self.loop,self.replacements,self.libs,self.name,self.type)
        return o
