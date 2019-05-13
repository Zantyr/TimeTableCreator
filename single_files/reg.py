from math import sqrt
def fun(X,Y,sym1="x", sym2="y", sym3="a", u1="m",u2="s", dY=0.1):
	sX,sY,sXX,sXY,N=0.0,0.0,0.0,0.0,0
	for i,x in enumerate(X):
		sX += x
		sXY += x * Y[i]
		sXX += x**2
		N+=1
	for y in Y:
		sY += y
	a = (N*sXY-sX*sY)/(N*sXX-sX*sX)
	da = 3*sqrt(N/(N-2) * (dY**2)/(N*sXX-sX*sX))
	print "sum "+sym1+" = " + str(sX) + " ~~~~~"
	print "sum "+sym2+" = " + str(sY) + " ~~~~~"
	print "sum "+sym1+sym2+" = " + str(sXY) + " ~~~~~"
	print "sum "+sym1+"^2 = " + str(sXX) + " newline"
	print sym3 + " = {N sum "+sym1+sym2+" - sum "+sym1+" sum "+sym2+"} over {N sum "+sym1+"^2 - sum ^2 "+sym1+"} = {"+str(N)+" cdot "+str(sXY)+u1+" cdot "+u2+" - "+str(sX)+u1+" cdot "+str(sY)+u2+"} over {"+str(N)+" cdot "+str(sXX)+u1+"^2 - "+str(sX**2)+u1+"^2} = "+str(a)+" "+u2+" over "+u1+" newline"
	print "%DELTA " + sym3 + " = 3 sqrt { N over {N-2} (%DELTA " + sym2 + ")^2 over {N sum "+sym1+"^2 - sum ^2 "+sym1+"}} = 3 sqrt { "+str(N)+" over "+str(N-2)+" {"+str(dY**2)+u2+"^2} over {"+str(N)+" cdot "+str(sXX)+u1+"^2 - "+str(sX**2)+u1+"^2}} = "+str(da)+" "+u2+" over "+u1+" newline"
	return

def get():
	X,Y=[],[]
	s = raw_input(">>")
	while(s):
		x,y = s.split("\t")
		x,y = x.replace(",","."),y.replace(",",".")
		x,y = float(x),float(y)
		X.append(x)
		Y.append(y)
		s = raw_input(">>")
	return X,Y

X,Y = get()
fun(X,Y)
