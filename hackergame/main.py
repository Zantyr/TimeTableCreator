from __future__ import print_function
from __future__ import division
from time import sleep
try: input=raw_input
except NameError: pass
from sys import argv
import pickle

"""
This module implement basic
"""

from stdlib import Machine

if __name__=="__main__":
    try:
        assert(len(argv)>1)
        with open(argv[1],"r") as f:
            vector = pickle.load(f)
    except AssertionError,IOError:
        try:
            from line import main
            vector = main()
        except ImportError:
            print("There is no default scenario - plain mode")
            vector=[Machine('192.168.0.0','speerrceok')]
    vector[0].sh(True)
    quit()
    path = input("Savefile: ")
    if path!='':
        with open(path,"w") as f:
            pickle.dump(vector,f,protocol=0) #get_iso_method
            print("Game saved succesfully")