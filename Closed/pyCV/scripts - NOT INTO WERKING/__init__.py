import plotsin
import viewdir

subscripts = {}

def extract(string):
	separator = "\n\n" #TUTAJ MUSI BYC LineBreakCarriageReturn
	header,data = string.split(separator)
	print header, data #DEBUG
	for i in list(subscripts):
		mess = re.search("OS=View.21",i)
		if mess:
			subscripts[i]()	
	return
