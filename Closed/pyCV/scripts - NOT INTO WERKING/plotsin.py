#EXAMPLES by Zantur

import matplotlib.pyplot as pl
from math import sin
from scripts import subscripts

def plotsin():
	x,y = [],[]
	for i in range(501):
		x.append(0.01*i)
	for i in x:
		y.append(sin(i))
	pl.plot(x,y)
	pl.show()
	return

subscripts["PLOT=Plot.21"] = plotsin
