from __future__ import print_function
from __future__ import division
from time import sleep
try: input=raw_input
except NameError: pass

"""
This module implement basic
"""

from stdlib import Machine

if __name__=="__main__":
    machine = Machine('192.168.0.0','speerrceok')
    machine.sh(True)