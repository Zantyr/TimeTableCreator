print "Loading the SCRIPT package..."

#creating whole-module vars
functions={}
howManyArgs={}
variables={}
IOsets={}
variables["True"]=1
variables["False"]=0
operator = "(\+|-|\*|\/|(\^)|(>>)|(<<)|(>=)|(<=)|(==)|(!=))"
numeric = "-?(\d+(\.\d*)?)"
identifier = "([A-Za-z_](\w)*)"
function = "(!\w(\w|\d)*)"
separator = "(,|;)"
string = "\"(.*)\""
modifier = "-(A-Za-z_)+"

#importing shit
from interpreter import *
from parseFile import *
from localRun import *
from server import *
