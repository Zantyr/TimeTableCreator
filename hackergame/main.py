from __future__ import print_function
from __future__ import division
from time import sleep
try: input=raw_input
except NameError: pass
from sys import argv
import json
import readline

"""
This module implement basic
"""

from stdlib import Machine

if __name__=="__main__":
    try:
        assert(len(argv)>1)
        with open(argv[1],"r") as f:
            vector = json.loads(f.read())
            vector = map(lambda x:Machine.from_dict(x),vector)
    except AssertionError,IOError:
        try:
            from line import main
            vector = main()
        except ImportError:
            print("There is no default scenario - plain mode")
            vector=[Machine('192.168.0.0','speerrceok')]
    vector[0].sh(True)
    path = input("Savefile: ")
    if path!='':
        with open(path,"w") as f:
            f.write(json.dumps(map(lambda x:x.to_dict(),vector))) #get_iso_method
            print("Game saved succesfully")