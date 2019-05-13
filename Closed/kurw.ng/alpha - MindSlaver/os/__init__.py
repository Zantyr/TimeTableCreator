import os

def viewDirectory(address):
	return os.listdir(address)

print viewDirectory("\\home")
