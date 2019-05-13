#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import re
import matplotlib.pyplot as pl
from math import sin
import os
import threading
import webbrowser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def rot13(STR):
	NEW,dic,pre,post = "",{}, "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM", "djreglhvbcnfqstuwxymkpioazDJREGLHVBCNFQSTUWXYMKPIOAZ"
	for i in xrange(len(pre)):
		dic[pre[i]] = post[i]
	for i in STR:
		try:
			NEW += (dic[i])
		except KeyError:
			NEW += i
	return NEW

global files
files={}

files["index.html"]="\n<ugzy><urnq><zrgn pbagrag=\"grkg/ugzy\" punefrg=\"hgs-8\">\n<gvgyr>Znlor V qvqa'g svavfu VG fghqvrf, ohg V'ir tbg orfg erfhzr lbh'ir cebonoyl frra.</gvgyr>\n<yvax ery=\"fglyrfurrg\" glcr=\"grkg/pff\" uers=\"pff.pff\"></urnq>\n<obql><qvi vq=\"one\">\n<qvi vq=\"oybd\"><n uers=\"rkcrevrapr.ugzy\">Zl rkcrevrapr</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"fxvyyf.ugzy\">Zl fxvyyf</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"vagrerfgf.ugzy\">Zl vagrerfgf</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"grfg.ugzy\">Grfg zr</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"pbagnpg.ugzy\">Pbagnpg zr</n></qvi>\n</qvi><oe>\n<pragre><v><u2>Zl anzr vf Cnjrł Gbznfvx. V'z 22 naq V ybir guvaxvat.</u2></v></pragre><oe>\n<c>Zl terngrfg nffrgf ner: nanylgvpny guvaxvat, syhrag pbzznaq bs Ratyvfu, haqrefgnaqvat bs Znguf naq Culfvpf, cebtenzzvat novyvgvrf.</c>\n<c>V nz yrneavat Clguba naq hfrq P++, UGZY, CUC, n yvggyr ovg bs WF, naq ZngYno. V svaq zlfrys yvxvat cebtenzzvat naq trggvat vg dhvgr rnfvyl, qrfcvgr yvggyr sbezny rqhpngvba va cnegvphyne qvfpvcyvarf. Ubjrire, V pna cerfrag lbh gur fbhepr pbqrf juvpu V'ir jevggra fb sne.</c>\n</qvi></obql></ugzy>"
files["contact.html"]="\n<ugzy><urnq><zrgn pbagrag=\"grkg/ugzy\" punefrg=\"hgs-8\">\n<gvgyr>Znlor V qvqa'g svavfu VG fghqvrf, ohg V'ir tbg orfg erfhzr lbh'ir cebonoyl frra.</gvgyr>\n<yvax ery=\"fglyrfurrg\" glcr=\"grkg/pff\" uers=\"pff.pff\"></urnq>\n<obql><qvi vq=\"one\">\n<qvi vq=\"oybd\"><n uers=\"rkcrevrapr.ugzy\">Zl rkcrevrapr</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"fxvyyf.ugzy\">Zl fxvyyf</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"vagrerfgf.ugzy\">Zl vagrerfgf</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"grfg.ugzy\">Grfg zr</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"pbagnpg.ugzy\">Pbagnpg zr</n></qvi>\n</qvi><oe>\n<qvi><pragre><v><u2>Yrg'f fgnl va gbhpu!</u2></v></pragre><oe>\n<c>Vs lbh'er ybbxvat sbe na rzcyblrr, na vagrea, be fvzcyl yvxr gb funer lbhe xabjyrqtr, svyy gur sbyybjvat sbez. Lbh pna nyfb svaq zr ba <n uers=\"uggc://yvaxrqva.pbz/va/cnjr%P5%82-gbznfvx-n27788o3\">YvaxrqVa</n>. Vs lbh'ir tbg nal dhrfgvbaf, be jnag n qverpg pbagnpg, zl r-znvy vf <n uers='znvygb:gbznfvx.xjvqmla@tznvy.pbz'>gbznfvx.xjvqmla@tznvy.pbz</n></c>\n</qvi>\n<qvi><pragre><u3>Fnir lbhefrys ba zl Pbagnpg Yvfg</u3></pragre><oe>\n<sbez npgvba=\"fnirq.ugzy\" zrgubq=\"CBFG\">\n<gnoyr><ge><gq>Lbhe anzr:</gq><gq><vachg anzr=\"anzr\"></gq></ge>\n<ge><gq>Lbhe pbzcnal:</gq><gq><vachg anzr=\"pbzcnal\"></gq></ge>\n<ge><gq>Gryy zr fbzrguvat nobhg jung lbh qb:</gq><gq><vachg anzr=\"fzgu\"></gq></ge></gnoyr>\n<c><vachg glcr='fhozvg' inyhr='Fhozvg'></c></sbez></qvi></sbez></obql></ugzy>\n"
files["css.css"]="\nobql {\n	sbag-snzvyl: zbabfcnpr;\n	yvar-urvtug: 1.5rz;\n	obeqre: 1ck qbggrq;\n	jvqgu: 650ck;\n	znk-jvqgu: 93ij;\n	znetva: 10ck nhgb;\n	cnqqvat: 5ck 0;\n}\nn {\n	grkg-qrpbengvba: abar;\n	pbybe: #000;\n	obeqre-obggbz: 1ck qbggrq;\n}\nn:ubire {\n	pbybe: #sss;\n	onpxtebhaq-pbybe: #000;\n	obeqre: 0ck;\n}\n#oybd {\n	qvfcynl:vayvar-oybpx;\n	onpxtebhaq-pbybe: #s9s9s9;\n	jvqgu: 18%;\n}"
files["experience.html"]="\n<ugzy><urnq><zrgn pbagrag=\"grkg/ugzy\" punefrg=\"hgs-8\">\n<gvgyr>Znlor V qvqa'g svavfu VG fghqvrf, ohg V'ir tbg orfg erfhzr lbh'ir cebonoyl frra.</gvgyr>\n<yvax ery=\"fglyrfurrg\" glcr=\"grkg/pff\" uers=\"pff.pff\"></urnq>\n<obql><qvi vq=\"one\">\n<qvi vq=\"oybd\"><n uers=\"rkcrevrapr.ugzy\">Zl rkcrevrapr</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"fxvyyf.ugzy\">Zl fxvyyf</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"vagrerfgf.ugzy\">Zl vagrerfgf</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"grfg.ugzy\">Grfg zr</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"pbagnpg.ugzy\">Pbagnpg zr</n></qvi>\n</qvi><oe>\n<qvi><pragre><v><u2>V nz bcra gb yrneavat</u2></v></pragre><oe>\n<c>Sbe n lrne V nz fhpprfshyyl pbaarpgvat fghqlvat grpuavpny gbcvpf jvgu jbex. Sbe arneyl unys n lrne V rnea nyy gur vapbzr V fcraq sbe zl yvivat.</c>\n<c>V fghql Grpuavpny Culfvpf ng Tqnńfx Havirefvgl bs Grpuabybtl, svavfuvat n onpurybe/ratvarre qrterr va Sro 2017. Zl fcrpvnyvfngvba eribyirf nebhaq pynffvp naq erarjnoyr raretl fbheprf. V unir n fbyvq onfr va ahzrevp zrgubqf naq pnyphyhf. V'ir <n uers=\"uggc://nevbpu.890z.pbz/PI/zng.cqs\">svavfurq fpvrapr pynffrf ng Uvtu Fpubby ab 1 va Xjvqmla.</n></c>\n<c>Zl pheerag ibpngvbany rkcrevrapr vf nf sbyybjf:</c>\n<gnoyr>\n<ge><gq>Crevbq</gq><gq>Pbzcnal</gq><gq>Pvgl</gq><gq>Wbo</gq><gq>Erfcbafvovyvgvrf</gq></ge>\n<ge><gq>Qrp 2015 - ...</gq><gq>Benatr</gq><gq>Tqnńfx</gq><gq>Qrnyre Fhccbeg</gq><gq>Irevsvpngvba bs qbphzragf nppbeqvat gb n frg bs cebprqherf, pbagebyyvat gur qrogf naq onynapr bs pyvragf</gq></ge>\n<ge><gq>Nht - Frc 2015</gq><gq>Wnovy Pvephvgf</gq><gq>Xjvqmla</gq><gq>Vairagbel Pbageby</gq><gq>Qryvirel bs ryrpgebavp pbzcbaragf jvgu ertneq gb fnsrgl ehyrf, cerqrsvarq cebqhpgvba fpurqhyr; vairagnevfngvba</gq></ge>\n<ge><gq>Why - Nht 2015</gq><gq>Pneersbhe</gq><gq>Xjvqmla</gq><gq>Pnfuvre</gq><gq>Znvagnvavat tbbq eryngvbafuvcf jvgu pyvragf, xrrcvat gur evtug onynapr</gq></ge>\n<ge><gq>Nce - Wha 2015</gq><gq>Grfpb</gq><gq>Tqnńfx</gq><gq>Cebqhpg Cynprzrag</gq><gq>Hacnpxvat gur cebqhpgf naq cynpvat gurz va na ngeenpgvir znaare</gq></ge>\n</gnoyr><c></c></qvi></sbez></obql>"
files["index.html"]="\n<ugzy><urnq><zrgn pbagrag=\"grkg/ugzy\" punefrg=\"hgs-8\">\n<gvgyr>Znlor V qvqa'g svavfu VG fghqvrf, ohg V'ir tbg orfg erfhzr lbh'ir cebonoyl frra.</gvgyr>\n<yvax ery=\"fglyrfurrg\" glcr=\"grkg/pff\" uers=\"pff.pff\"></urnq>\n<obql><qvi vq=\"one\">\n<qvi vq=\"oybd\"><n uers=\"rkcrevrapr.ugzy\">Zl rkcrevrapr</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"fxvyyf.ugzy\">Zl fxvyyf</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"vagrerfgf.ugzy\">Zl vagrerfgf</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"grfg.ugzy\">Grfg zr</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"pbagnpg.ugzy\">Pbagnpg zr</n></qvi>\n</qvi><oe>\n<pragre><v><u2>Zl anzr vf Cnjrł Gbznfvx. V'z 22 naq V ybir guvaxvat.</u2></v></pragre><oe>\n<c>Zl terngrfg nffrgf ner: nanylgvpny guvaxvat, syhrag pbzznaq bs Ratyvfu, haqrefgnaqvat bs Znguf naq Culfvpf, cebtenzzvat novyvgvrf.</c>\n<c>V nz yrneavat Clguba naq hfrq P++, UGZY, CUC, n yvggyr ovg bs WF, naq ZngYno. V svaq zlfrys yvxvat cebtenzzvat naq trggvat vg dhvgr rnfvyl, qrfcvgr yvggyr sbezny rqhpngvba va cnegvphyne qvfpvcyvarf. Ubjrire, V pna cerfrag lbh gur fbhepr pbqrf juvpu V'ir jevggra fb sne.</c>\n</qvi></obql></ugzy>"
files["interests.html"]="<ugzy><urnq><zrgn pbagrag=\"grkg/ugzy\" punefrg=\"hgs-8\">\n<gvgyr>Znlor V qvqa'g svavfu VG fghqvrf, ohg V'ir tbg orfg erfhzr lbh'ir cebonoyl frra.</gvgyr>\n<yvax ery=\"fglyrfurrg\" glcr=\"grkg/pff\" uers=\"pff.pff\"></urnq>\n<obql><qvi vq=\"one\">\n<qvi vq=\"oybd\"><n uers=\"rkcrevrapr.ugzy\">Zl rkcrevrapr</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"fxvyyf.ugzy\">Zl fxvyyf</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"vagrerfgf.ugzy\">Zl vagrerfgf</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"grfg.ugzy\">Grfg zr</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"pbagnpg.ugzy\">Pbagnpg zr</n></qvi>\n</qvi><oe>\n<qvi><pragre><v><u2>V nz arneyl nyjnlf phevbhf</u2></v></pragre><oe>\n<c></c>\n<c>V'ir yrnq n <n uers=\"uggc://jjj.ynfg.sz/zhfvp/Qrss+Havxbeam\">fznyy ryrpgebavp zhfvp cebwrpg</n> va uvtu-fpubby bhg bs oberqbz. V <n uers=\"uggc://nevbpu.890z.pbz/PI/zhm.cqs\">svavfurq svefg-tenqr zhfvp fpubby ba fnkbcubar.</n></c>\n<c>V nz fbzrjung vagrerfgrq va GPT Zntvp: gur Tngurevat. V hfrq gb cynl pbzchgre tnzrf, ohg V eneryl qb vg abj.</c>\n<c>V yvxr ernqvat negvpyrf ba gur vagrearg ertneqvat qvirefr znggre. V cersre ernqvat aba-svpgvba bire zbivrf naq fgbevrf.</c></qvi></obql></ugzy>"
files["saved.html"]="\n<ugzy>\nLbhe pbagnpg unf orra fnirq.\n</ugzy>"
files["skills.html"]="\n<ugzy><urnq><zrgn pbagrag=\"grkg/ugzy\" punefrg=\"hgs-8\">\n<gvgyr>Znlor V qvqa'g svavfu VG fghqvrf, ohg V'ir tbg orfg erfhzr lbh'ir cebonoyl frra.</gvgyr>\n<yvax ery=\"fglyrfurrg\" glcr=\"grkg/pff\" uers=\"pff.pff\"></urnq>\n<obql><qvi vq=\"one\">\n<qvi vq=\"oybd\"><n uers=\"rkcrevrapr.ugzy\">Zl rkcrevrapr</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"fxvyyf.ugzy\">Zl fxvyyf</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"vagrerfgf.ugzy\">Zl vagrerfgf</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"grfg.ugzy\">Grfg zr</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"pbagnpg.ugzy\">Pbagnpg zr</n></qvi>\n</qvi><oe>\n<qvi><pragre><v><u2>V nz n serr guvaxre</u2></v></pragre><oe>\n<c><v>N gehr fubjpnfr bs zl cebtenzzvat fxvyyf vf gb or sbhaq ng \"Grfg zr\" cneg</v></c>\n<c>V nz ivrjrq ol zl crref nf n engure vagryyvtrag crefba. Qhevat uvtu-fpubby V cnegvpvcngrq va inevbhf pbzcrgvgvbaf \n<n uers=\"uggc://nevbpu.890z.pbz/PI/qvc1.cqs\">jvgu</n> \n<n uers=\"uggc://nevbpu.890z.pbz/PI/qvc2.cqs\">fbzr</n> \n<n uers=\"uggc://nevbpu.890z.pbz/PI/qvc3.cqs\">cerggl</n> \n<n uers=\"uggc://nevbpu.890z.pbz/PI/qvc4.cqs\">ovt</n> \n<n uers=\"uggc://nevbpu.890z.pbz/PI/qvc5.cqs\">fhpprffrf</n>, nygubhtu V xabj guvf vf abg gur zbfg vzcbegnag cneg.</c>\n<c>V nz n abivpr cebtenzzre. V'z pheeragyl qrirybcvat zl fxvyyf va Clguba, nygubhtu V unir n onfvp xabjyrqtr bs P++, naq gur zbfg vzcbegnag jro grpuabybtvrf. </c>\n<c>V srry dhvgr pbzsbegnoyr fcrnxvat Ratyvfu, nygubhtu V srry orggre jvgu jevggra ynathntr. V'ir cnffrq O2 rknz jvgu n irel tbbq tenqr.</c></qvi></obql></ugzy>"
files["test.html"]="\n<ugzy><urnq><zrgn pbagrag=\"grkg/ugzy\" punefrg=\"hgs-8\">\n<gvgyr>Znlor V qvqa'g svavfu VG fghqvrf, ohg V'ir tbg orfg erfhzr lbh'ir cebonoyl frra.</gvgyr>\n<yvax ery=\"fglyrfurrg\" glcr=\"grkg/pff\" uers=\"pff.pff\"></urnq>\n<obql><qvi vq=\"one\">\n<qvi vq=\"oybd\"><n uers=\"rkcrevrapr.ugzy\">Zl rkcrevrapr</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"fxvyyf.ugzy\">Zl fxvyyf</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"vagrerfgf.ugzy\">Zl vagrerfgf</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"grfg.ugzy\">Grfg zr</n></qvi>\n<qvi vq=\"oybd\"><n uers=\"pbagnpg.ugzy\">Pbagnpg zr</n></qvi>\n</qvi><oe>\n<qvi><pragre><v><u2>Grfg zl fxvyyf.</u2></v></pragre><oe>\n<c><v>Pheeragyl gur sbezhynf unir gb or ragrerq jvgu fcnprf orgjrra rnpu gbxra.</v></c>\n<gnoyr><ge>\n<sbez npgvba=\"grfg.ugzy\" zrgubq=\"CBFG\"><gq><fcna>Qvfcynl n cybg bs n shapgvba (zngcybgyvo): </fcna></gq><gq><vachg glcr=\"grkg\" anzr=\"RKC\" inyhr=\"k ^ 2 + 3\"></gq><gq><vachg glcr=\"fhozvg\" anzr=\"CYBG\" inyhr=\"Cybg!\"></vachg></gq></sbez></ge>\n<ge><sbez npgvba=\"grfg.ugzy\" zrgubq=\"CBFG\"><gq><fcna>Pnyphyngr na rkcerffvba sbe lbh: </fcna></gq><gq><vachg glcr=\"grkg\" anzr=\"RKC\" inyhr=\"k ^ 2 + 3\"></gq><gq><vachg glcr=\"fhozvg\" anzr=\"PNYP\" inyhr=\"Pbzchgr!\"></gq></sbez>\n</ge></gnoyr><oe>\n<c>Lbh pna nyfb ivfvg <n uers=\"uggc://jjj.tvguho.pbz/Mnagle\">zl TvgUho nppbhag</n> sbe zber ersreraprf gb zl cebtenzzvat.</c></qvi></sbez></obql>"

try:
	import matplotlib.pyplot as pl
	PLOTTABLE = True
except ImportError:
	print "Cannot import matplotlib"
	PLOTTABLE = False

global toOpen
functions,howManyArgs={},{}
DIR = "CV"

def add(*args):
	try:
		return args[0]+args[1]
	except TypeError:
		print args[0],args[1],"BUONT TYPU"

def sub(*args):
	try:
		return args[0]-args[1]
	except TypeError:
		print args[0],args[1],"BUONT TYPU"

def mul(*args):
	try:
		return args[0]*args[1]
	except TypeError:
		print args[0],args[1],"BUONT TYPU"

def div(*args):
	try:
		return args[0]/args[1]
	except TypeError:
		print args[0],args[1],"BUONT TYPU"

def power(*args):
	try:
		return pow(args[0],args[1])
	except TypeError:
		print args[0],args[1],"BUONT TYPU"

functions["+"]=add
functions["-"]=sub
functions["*"]=mul
functions["/"]=div
functions["^"]=power
howManyArgs["+"]=2
howManyArgs["-"]=2
howManyArgs["*"]=2
howManyArgs["/"]=2
howManyArgs["^"]=2

def whatType(arg):
	try:
		x = 2.0  + arg
		return "numeric"
	except TypeError:
		try:
			if(arg=="x"): return "identifier"
			else: return None
		except TypeError:
			if(isList(arg)): return "list"
			else: return None

def assoc(i):
	left=["+","-","*","/"]
	if i in left: return True
	else: return False

def precedence(i,j):
	pre = {}
	pre["("]=-4
	pre["+"]=1
	pre["-"]=1
	pre["*"]=2
	pre["/"]=2
	pre["^"]=3
	pre[")"]=99
	if((pre[i]<=pre[j] and assoc(i)) or (pre[i]<pre[j] and assoc(i))): return True
	else: return False

def upgradedSplit(strin):
	ret = strin.split(" ")
	return ret

def shuntingYard(strin):
	operator = "(\+|-|\*|\/|(\^)|sin|cos|tan|tg|cotan|ctg|ln|exp)"
	numeric = "-?(\d+(\.\d*)?)"
	identifier = "(x)"
	left = "\("
	right = "\)"
	output = []
	stack = []
	tokens = upgradedSplit(strin)
	for token in tokens:
		x = re.match(numeric,token)
		if(x): 
			output.append(float(x.group(1)))
			continue
		x = re.match(identifier,token)		
		if(x): output.append(x.group(1))
		x = re.match(operator,token)
		if(x):
			op = x.group(1)
			while(len(stack)):
				temp = stack.pop()
				if(precedence(op,temp)):output.append(temp)
				else:
					stack.append(temp)				
					break
			stack.append(op)
		x = re.match(left,token)
		if(x): stack.append("(")
		x = re.match(right,token)
		if(x):
			while(len(stack)):
				temp = stack.pop()
				if(temp=="("):
					stack.append(temp)
					if(len(stack)):
						temp = stack.pop()
						if re.match(function,temp): output.append(temp)
					break
				else:
					output.append(temp)
	while(len(stack)):
		temp = stack.pop()
		if all((temp!="(",temp!=")")): output.append(temp)
		else: return False
	return output

def evaluate(strinput, val=0):
	operator = "(\+|-|\*|\/|(\^)|sin|cos|tan|tg|cotan|ctg|ln)"
	numeric = "-?(\d+(\.\d*)?)"
	identifier = "(x)"
	stack = []
	postfix = shuntingYard(strinput)
	for i in postfix:
		#print stack
		if whatType(i)=="numeric":stack.append(i)
		if whatType(i)=="identifier": stack.append(val)
		try:
			if re.match(operator,str(i)):
				args=[]
				for j in range(howManyArgs[i]):
					args = [stack.pop()] + args
				stack.append(functions[i](*args))
		except TypeError:
			print "KURWA BUONT TYPU"
	if(len(stack)>1):return None
	return stack[0]

def plotfun(asc,scale=10):
	x,y = [],[]
	for i in range(200):
		print i
		x.append((scale/100.0)*i-scale)
		y.append(evaluate(asc,(scale/100.0)*i-scale))
	print x,y
	pl.plot(x,y)
	pl.show()

def openWeb():
	webbrowser.open('http://localhost:1488')

def viewhome():
	ls = os.listdir("\\home")
	for i in ls:
		print ls
	return

def getMessage(toOpen):
	global DIR,files
	header = "HTTP/1.1\nContent-Type: text/html; charset=UTF-8\n\n"
	if(toOpen[:6] == "<html>"):
		return header + toOpen
	message = rot13(files[toOpen])
	return header + message

def HTTPtostr(asc):
	asc = asc.replace("+"," ")
	while(re.search("%[0-9A-F]{2}",asc)):
		x = re.search("%([0-9A-F]{2})",asc).group(1)
		asc = asc.replace("%"+x,x.decode("hex"))
		print x, asc
	return asc

def addToNotepad(asc):
	x = re.search("name=([^&]*)&company=([^&]*)&smth=([^&]*)",asc)
	name = HTTPtostr(x.group(1))
	company = HTTPtostr(x.group(2))
	smth = HTTPtostr(x.group(3))
	with open("notes.dat","a") as f:
		f.write("Name: " + name + "\nCompany: " + company + "\nFew words: " + smth + "\n\n")

def addToDB(asc):
	sender="ariochcv@gmail.com"
	receivers=["tomasik.kwidzyn@gmail.com"]
	pwd = "klopsiki"
	x = re.search("name=([^&]*)&company=([^&]*)&smth=([^&]*)",asc)
	name = HTTPtostr(x.group(1))
	company = HTTPtostr(x.group(2))
	smth = HTTPtostr(x.group(3))
	message="<html><head><meta content='text/html' charset='utf-8'></head><body>Oto wpisane dane:<br>Nazwa:" + name + "<br>Kompania:" + company + "<br>Opis: "+ smth+"</body></html>"
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Nowa odpowiedz na CV!"
	msg['From'] = sender
	msg['To'] = receivers[0]
	msg.attach(MIMEText(message, 'html','utf-8'))
	s = smtplib.SMTP( "smtp.gmail.com:587")
	s.ehlo()
	s.starttls()
	s.login(sender,pwd)
	s.sendmail(sender, receivers, msg.as_string())
	s.quit()

def extract(string):
	global toOpen
	try:
		mess = re.search("EXP=(.*)&PLOT=Plot.21",string)
		if mess:
			print HTTPtostr(mess.group(1))
			plotfun(HTTPtostr(mess.group(1)),10)
			return
	except:
		print "Nought"
		mess = ""
	try:
		mess = re.search("EXP=(.*)&CALC=Compute.21",string)
		if mess:
			toOpen = "<html><body><center>Wynik to: " + str(evaluate(HTTPtostr(mess.group(1)))) +  "</center></body></html>"
			return
	except:
		print "Nought"
		mess = ""
	try:
		mess = re.search("(name=[^&]*&company=[^&]*&smth=[^&]*)",string)
		if mess:
			addToDB(mess.group(1))
			return
	except TypeError:
		print "Nought"
		mess = ""

#MAIN HTML SERVER

PORT = 1488
BUFFERSIZE=1024
net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
net.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
net.bind(('', PORT))
th = threading.Thread(target=openWeb)
th.run()
while(1):
	print "Port Estabilished"
	net.listen(2)
	(clientsocket, address) = net.accept()
	print "Socket Created"
	data = clientsocket.recv(BUFFERSIZE)
	print data
	try:
		toOpen = re.search("(GET|POST) .(.*\.(html|css|jpg))",data).group(2)
		print "FILE TO BE FOUND: " + toOpen
	except:
		print "Error Occured - no page found - returning HOME"
		toOpen = "index.html"
	extract(data)
	message = getMessage(toOpen)
	clientsocket.send(message)
	clientsocket.close()
	print "Page Sent"
net.shutdown(socket.SHUT_RDWR)
net.close(socket.SHUT_RDWR)
