#QVICKSILVER PID
#for fast Arduino measurement/regulation modules

#in this file:
#   headers
#   creation of a device from a list of commands
#   execution of device
#   command line workings

import arduino
import creator
import properties as P
import sys

if __name__ == "__main__":
    try:
        with open(sys.argv[1],"r") as f:
            listtobeprocessed = []
            for line in f:
                line = line.strip()
                if line!="" and line[0]!="#":
                    listtobeprocessed.append(line)
    except IndexError:
        listtobeprocessed = creator.main()
    except IOError:
        print "Exception: The input file could not be found. Aborting..."
        quit()
    dev = arduino.Arduino()
    o1 = dev.add("thermal_iterator") #add output
    dev.add("diode_output",o1) #add output
    o2 = dev.add("thermal_iterator") #add output
    dev.add("diode_output",o2) #add output
    print dev.build()
