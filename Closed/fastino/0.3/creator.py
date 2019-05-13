#this function runs a wizard that easily creates a proper device by asking from prompt for needed devices, and other building blocks
#can also give help and create a device from file, can store, push and pull from server different schematics and libs

#this returns a list of commands
def main():
    return []

'''
syntax:

accepted are lines in any form; only lines in a form given below are considered:
command[ params]+;

commands:
ino         DEVICE TYPE DECLARATION
dev         CREATION OF A DEV
opt         PASSING A PARAMETER
grep        CATCHING AN OUTPUT
pass        PASSING AN INPUT
'''