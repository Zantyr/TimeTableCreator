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

def version(verstr=None):
    VERSION = (0,2,0)
    if verstr==None:
        return '.'.join([str(x) for x in VERSION])
    else:
        verstr = [int(x) for x in verstr.split('.')]
        for i,j in zip(VERSION,verstr):
            if i<j:
                return False
        return True

from stdlib import Machine

if __name__=="__main__":
    try:
        assert(len(argv)>1)
        with open(argv[1],"r") as f:
            save = json.loads(f.read())
            if not version(save['version']):
                print('Savefile in incompatible version. Terminating.')
                quit()
            vector = save['save']
            vector = map(lambda x:Machine.from_dict(x),vector)
            for machine in vector:
                new_network = {}
                for client in machine.network:
                    new_network[client] = vector[[x.ip_address for x in vector].index(client)]
                machine.network = new_network
    except AssertionError,IOError:
        try:
            import line
            vector = line.main()
        except ImportError:
            print("There is no default scenario - plain mode")
            vector=[Machine('192.168.0.0','speerrceok')]
    vector[0].sh(True)
    try:
        assert(len(argv)>1)
        path = argv[1]
    except AssertionError:
        path = input("Savefile: ")
    if path!='':
        with open(path,"w") as f:
            f.write(json.dumps({'version':version(),'save':map(lambda x:x.to_dict(),vector)})) #get_iso_method
            print("Game saved succesfully")