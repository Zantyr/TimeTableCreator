import re
print "Estymator Seebecka"
string = "Ag 	0,73 	Fe 	11,6 	Nb 	1,05 	Sr 	-3Al 	-2,2 	Ga 	0,5 	Nd 	-4 	Ta 	0,7Au 	0,82 	Gd 	-4,6 	Ni 	-8,5 	Tb 	-1,6Ba 	-4 	Hf 	0 	Np 	8,9 	Th 	0,6Be 	-2,5 	Ho 	-6,7 	Os 	-3,2 	Ti 	-2Ca 	1,05 	In 	0,56 	Pb 	-0,58 	Tl 	0,6Cd 	-0,05 	Ir 	1,42 	Pd 	1,1 	Tm 	-1,3Ce 	13,6 	K 	-5,2 	Pu 	12 	U 	3Co 	-8,43 	La 	0,1 	Rb 	-3,6 	V 	2,9Cr 	5 	Li 	4,3 	Re 	-1,4 	W 	-4,4Lu 	-6,9 	Rh 	0,8 	Y 	-5,1Cu 	1,19 	Mg 	-2,1 	Ru 	0,3 	Yb 	5,1Dy 	-4,1 	Mn 	-2,5 	Sc 	-14,3 	Zn 	0,7Er 	-3,8 	Mo 	0,1 	Sm 	0,7 	Zr 	4,4Eu 	5,3 	Na 	-2,6 	Sn 	-0,04 	"
nd,allcombos,comp, srted = {}, {}, {}, []
while(re.search("([A-Za-z]+)[\s]*(-?\d*,\d*)(.*)",string)):
	x = re.search("([A-Za-z]+)[\s]*(-?\d*,\d*)(.*)",string)
	string = x.group(3)
	nd[x.group(1)] = float(x.group(2).replace(",","."))
for i in range(len(list(nd))-1):
	for j in range(i+1,len(list(nd))):
		allcombos[list(nd)[i] + list(nd)[j]] = nd[list(nd)[i]] - nd[list(nd)[j]]
estim = float(raw_input("Podaj wyliczony wspolczynnik Seebecka: "))
for i in list(allcombos):
	comp[i] = abs(allcombos[i]-estim)
for i in list(comp):
	srted.append(comp[i])
srted.sort()
print "Najblizsze trafienia: "
for i in list(comp):
	if comp[i] in srted[:3]: print "    " + i + ": " + str(allcombos[i])
