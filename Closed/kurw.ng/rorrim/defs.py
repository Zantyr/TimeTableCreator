#this file contains constants and variables, lol

#main settings
VERBOSE = False #for debug
ASKFORFILE = False
DEFAULTSCRIPT = "script.xD"
MODESELECT = True
DEFAULTLISTEN = True
doIWannaListen = False
doIWannaLocal = False

#containers for interpreter memory and constants
functions={}
howManyArgs={}
variables={}
IOsets={}
variables["True"]=1
variables["False"]=0
variables["pi"]=3.14

#tokens for evaluating the token type (regexp)
token_operator = "(\+|-|\*|\/|(\^)|(>>)|(<<)|(>=)|(<=)|(==)|(!=))"
token_numeric = "-?(\d+(\.\d*)?)"
token_identifier = "([A-Za-z_](\w)*)"
token_function = "(!\w(\w|\d)*)"
token_separator = "(,|;)"
token_string = "\"(.*)\""
token_modifier = "-(A-Za-z_)+"
token_uprgraded_split_string = "(.*)(\"[^\"\n]*\")(.*)"

#keywords for parser
keyword_branching = ["dopoki ","jesli ","definicja "]
keyword_rebranching = ["ilsej","ikopod","ajcinifed"]

#syntax - sentence types:
syntax_assignment = "([A-Za-z_](\w)*) ?= ?(.*)"
syntax_call = "![A-Za-z_](\w)*"
syntax_return = "return [A-Za-z_](\w)*"
syntax_defun = "definicja ([A-Za-z_](\w)*)"
syntax_while = "dopoki (([^n]*))"
syntax_conditional = "jesli (([^n]*))"
