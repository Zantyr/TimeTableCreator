#EXAMPLES by Zantur

from scripts import subscripts

def viewhome():
	ls = os.listdir("\\home")
	for i in ls:
		print ls
	return

subscripts["OS=View.21"] = viewhome
