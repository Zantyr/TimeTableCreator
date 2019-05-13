import re
import sys
debug = False
zmienne = {}
labele = {}
kod = []
#iof = raw_input("Dzien dobry. Prosze podaj plik wejsciowy: ")
iof = "/home/zantyr/Kody/Kurwing/kurw.in"
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_key(s):
	try:
		zmienne[s]
		return True
	except KeyError:
		return False

#labelinit
i = -1
with open(iof) as file:
	for line in file:
		i += 1
		kod.append(line)
		inp = re.search("#([^\n \t]+)",line)
		if inp is not None:
			zmienna = str(inp.group(1))
			labele[zmienna] = i

#loopinit
i = -1

def evaluate(exp):
	global zmienne
	inp = re.search("([^\n \t]+) [Tt][Oo] [Nn][Ii][Ee] ([^\n \t]+)",exp)
	if inp is not None:
		zmienna = inp.group(1)
		wartosc = inp.group(2)
		if is_number(wartosc):
			wartosc = str(float(wartosc))
		if zmienne[zmienna] != zmienne[wartosc]:
			return True
		return False
	inp = re.search("([^\n \t]+) [Tt][Oo] ([^\n \t]+)",exp)
	if inp is not None:
		zmienna = inp.group(1)
		wartosc = inp.group(2)
		if is_number(wartosc):
			wartosc = str(float(wartosc))
		if zmienne[zmienna] == zmienne[wartosc]:
			return True
		return False
	inp = re.search("([^\n \t]+) [Nn][Ii][Ee] [Bb][Rr][Zz][Mm][Ii] ([^\n]+)",exp)
	if inp is not None:
		zmienna = inp.group(1)
		wartosc = inp.group(2)
		if is_number(wartosc):
			wartosc = str(float(wartosc))
		if zmienne[zmienna] != wartosc:
			return True
		return False
	inp = re.search("([^\n \t]+) [Bb][Rr][Zz][Mm][Ii] ([^\n]+)",exp)
	if inp is not None:
		zmienna = inp.group(1)
		wartosc = inp.group(2)
		if is_number(wartosc):
			wartosc = str(float(wartosc))
		if zmienne[zmienna] == wartosc:
			return True
		return False

def expression(line="Wypierdalaj"):
	global debug	
	global zmienne
	global labele
	global i
	#debug
	inp = re.search("[Dd][Ee][Bb][Uu][Gg]",line)
	if inp is not None:
		debug = not debug
		return
	#assignment
	inp = re.search("[Nn][Ii][Ee][Cc][Hh] ([^\n \t]+) [Tt][Oo] ([^\n]+)",line)
	if inp is not None:
		zmienna = inp.group(1)
		wartosc = inp.group(2)
		wartosc = str(wartosc)
		if is_number(wartosc):
			wartosc = str(float(wartosc))
		if is_key(wartosc):
			wartosc = zmienne[wartosc]
		zmienne[zmienna] = str(wartosc)
		return
	inp = re.search("[Nn][Ii][Ee][Cc][Hh] ([^\n \t]+) [Bb][Rr][Zz][Mm][Ii] ([^\n]+)",line)
	if inp is not None:
		zmienna = inp.group(1)
		wartosc = inp.group(2)
		wartosc = str(wartosc)
		if is_number(wartosc):
			wartosc = str(float(wartosc))
		zmienne[zmienna] = str(wartosc)
		return
	#concatenate
	inp = re.search("[Dd][Oo][Jj][Ee][Bb] ([^\n \t]+) [Dd][Oo] ([^\n \t]+) [Bb][Ee][Zz] [Ss][Pp][Aa][Cc][Jj][Ii]",line)
	if inp is not None:
		zmienna = inp.group(2)
		wartosc = inp.group(1)
		zmienne[zmienna] = str(zmienne[zmienna]) + str(zmienne[wartosc])
		return
	inp = re.search("[Dd][Oo][Jj][Ee][Bb] ([^\n \t]+) [Dd][Oo] ([^\n \t]+)",line)
	if inp is not None:
		zmienna = inp.group(2)
		wartosc = inp.group(1)
		pomoc = str(zmienne[zmienna]) + " " + str(zmienne[wartosc])
		zmienne[zmienna] = str(pomoc)
		return
	#std output
	inp = re.search("[Ww][Yy][Jj][Ee][Bb] ([^\n \t]+) [Nn][Aa] [Ee][Kk][Rr][Aa][Nn] [Bb][Ee][Zz] [Ee][Nn][Tt][Ee][Rr][Aa]",line)
	if inp is not None:
		wartosc = inp.group(1)
		sys.stdout.write(zmienne[wartosc])
		return
	inp = re.search("[Ww][Yy][Kk][Uu][Rr][Ww] ([^\n \t]+) [Nn][Aa] [Ee][Kk][Rr][Aa][Nn] [Bb][Ee][Zz] [Ee][Nn][Tt][Ee][Rr][Aa]",line)
	if inp is not None:
		wartosc = inp.group(1)
		sys.stdout.write(zmienne[wartosc])
		return
	inp = re.search("[Ww][Yy][Jj][Ee][Bb] ([^\n \t]+) [Nn][Aa] [Ee][Kk][Rr][Aa][Nn]",line)
	if inp is not None:
		wartosc = inp.group(1)
		print(zmienne[wartosc])
		return
	inp = re.search("[Ww][Yy][Kk][Uu][Rr][Ww] ([^\n \t]+) [Nn][Aa] [Ee][Kk][Rr][Aa][Nn]",line)
	if inp is not None:
		wartosc = inp.group(1)
		print(zmienne[wartosc])
		return
	#ujeb
	inp = re.search("[Uu][Jj][Ee][Bb] ([^\n \t]+)",line)
	if inp is not None:
		zmienna = inp.group(1)
		pomoc = float(zmienne[zmienna])
		jebanko = int(pomoc)
		pomoc = float(jebanko)
		zmienne[zmienna] = str(pomoc)
	#zapytaj
	inp = re.search("[Zz][Aa][Pp][Yy][Tt][Aa][Jj] [Oo] ([^\n \t]+) [Ss][Ll][Oo][Ww][Aa][Mm][Ii] ([^\n]+)",line)
	if inp is not None:
		zmienna = inp.group(1)
		pomoc = inp.group(2)
		wartosc = raw_input(pomoc + " ")
		wartosc = str(wartosc)
		if is_number(wartosc):
			wartosc = str(float(wartosc))		
		zmienne[zmienna] = wartosc
		return

	inp = re.search("[Zz][Aa][Pp][Yy][Tt][Aa][Jj] [Oo] ([^\n \t]+)",line)
	if inp is not None:
		zmienna = inp.group(1)
		string = "Podaj, kurwa, " + zmienna + ": "
		wartosc = raw_input(string)
		wartosc = str(wartosc)
		if is_number(wartosc):
			wartosc = str(float(wartosc))		
		zmienne[zmienna] = wartosc
		return
	#zaloz harem
	inp = re.search("[Zz][Aa][Ll][Oo][Zz] [Hh][Aa][Rr][Ee][Mm] ([^\n \t]+)",line)	
	if inp is not None:	
		wartosc = str(inp.group(1))
		zmienne[wartosc] = "#H\n"
		return
	#wjeb do haremu
	inp = re.search("[Ww][Jj][Ee][Bb] ([^\n \t]+) [Ww] ([Hh][Aa][Rr][Ee][Mm] )*([^\n \t]+)",line)	
	if inp is not None:	
		wartosc = str(inp.group(3))
		zmienna = str(inp.group(1))
		zmienne[wartosc] = zmienne[wartosc] + zmienne[zmienna] + "\n"
		return
	#wyjeb z haremu w pizdu
	inp = re.search("[Ww][Yy][Jj][Ee][Bb] [Kk][Uu][Rr][Ww][Ee] [Nn][Uu]?[Mm]?[Ee]?[Rr] ([^\n \t]+) [Zz] ([^\n \t]+) [Ww] [Pp][Ii][Zz][Dd][Uu]",line)	
	if inp is not None:	
		pomoc = inp.group(1)
		if is_key(pomoc):
			pomoc = int(zmienne[pomoc])
		else:
			pomoc = int(pomoc)
		wartosc = inp.group(2)
		parsing = re.findall("[^\n]+",zmienne[wartosc])
		jebanko = ""
		for x,zmienna in enumerate(parsing):
			if x != pomoc:
				jebanko = jebanko + zmienna + "\n"
		zmienne[wartosc] = jebanko
		return
	#wyjeb z haremu
	inp = re.search("[Ww][Yy][Jj][Ee][Bb] [Kk][Uu][Rr][Ww][Ee] [Nn][Uu]?[Mm]?[Ee]?[Rr] ([^\n \t]+) [Zz] ([^\n \t]+) [Dd][Oo] ([^\n \t]+)",line)	
	if inp is not None:	
		pomoc = inp.group(1)
		if is_key(pomoc):
			pomoc = int(float(zmienne[pomoc]))
		else:
			pomoc = int(pomoc)
		wartosc = inp.group(2)
		zmienna = inp.group(3)
		parsing = re.findall("[^\n]+",zmienne[wartosc])
		wartosc = str(parsing[pomoc])		
		zmienne[zmienna] = wartosc
		return
	#dodaj
	inp = re.search("[Dd][Oo][Dd][Aa][Jj] ([^\n \t]+) [Dd][Oo] ([^\n \t]+)",line)
	if inp is not None:
		wartosc = str(inp.group(1))
		zmienna = str(inp.group(2))
		if is_number(wartosc) and is_number(zmienne[zmienna]):
			a = float(wartosc)
			b = float(zmienne[zmienna])
			zmienne[zmienna] = str(a+b)
			return
		if is_number(zmienne[wartosc]) and is_number(zmienne[zmienna]):
			a = float(zmienne[wartosc])
			b = float(zmienne[zmienna])
			zmienne[zmienna] = str(a+b)
		else:
			print("Podane kurwy nie sa liczbami.")
		return
	#odejmij
	inp = re.search("[Oo][Dd][Ee][Jj][Mm][Ii][Jj] ([^\n \t]+) [Oo][Dd] ([^\n \t]+)",line)
	if inp is not None:
		wartosc = str(inp.group(1))
		zmienna = str(inp.group(2))
		if is_number(wartosc) and is_number(zmienne[zmienna]):
			a = float(wartosc)
			b = float(zmienne[zmienna])
			zmienne[zmienna] = str(b-a)
			return
		if is_number(zmienne[wartosc]) and is_number(zmienne[zmienna]):
			a = float(zmienne[wartosc])
			b = float(zmienne[zmienna])
			zmienne[zmienna] = str(b-a)
		else:
			print("Podane kurwy nie sa liczbami.")
		return
	#mnozenie
	inp = re.search("[Pp][Rr][Zz][Ee][Mm][Nn][Oo][Zz] ([^\n \t]+) [Pp][Rr][Zz][Ee][Zz] ([^\n \t]+)",line)
	if inp is not None:
		wartosc = str(inp.group(2))
		zmienna = str(inp.group(1))
		if is_number(wartosc) and is_number(zmienne[zmienna]):
			a = float(wartosc)
			b = float(zmienne[zmienna])
			zmienne[zmienna] = str(a*b)
			return
		if is_number(zmienne[wartosc]) and is_number(zmienne[zmienna]):
			a = float(zmienne[wartosc])
			b = float(zmienne[zmienna])
			zmienne[zmienna] = str(a*b)
		else:
			print("Podane kurwy nie sa liczbami.")
		return
	#modulo
	inp = re.search("[Mm][Oo][Dd][Uu][Ll][Oo] ([Zz] )?([^\n \t]+) [Pp][Rr][Zz][Ee][Zz] ([^\n \t]+)",line)
	if inp is not None:
		wartosc = str(inp.group(3))
		zmienna = str(inp.group(2))
		if is_number(wartosc) and is_number(zmienne[zmienna]):
			a = float(wartosc)
			b = float(zmienne[zmienna])
			zmienne[zmienna] = str(b%a)
			return
		if is_number(zmienne[wartosc]) and is_number(zmienne[zmienna]):
			a = float(zmienne[wartosc])
			b = float(zmienne[zmienna])
			zmienne[zmienna] = str(b%a)
		else:
			print("Podane kurwy nie sa liczbami.")
		return
	#dzielenie
	inp = re.search("[Pp][Oo][Dd][Zz][Ii][Ee][Ll] ([^\n \t]+) [Pp][Rr][Zz][Ee][Zz] ([^\n \t]+)",line)
	if inp is not None:
		wartosc = str(inp.group(2))
		zmienna = str(inp.group(1))
		if is_number(wartosc) and is_number(zmienne[zmienna]):
			a = float(wartosc)
			b = float(zmienne[zmienna])
			zmienne[zmienna] = str(b/a)
			return
		if is_number(zmienne[wartosc]) and is_number(zmienne[zmienna]):
			a = float(zmienne[wartosc])
			b = float(zmienne[zmienna])
			zmienne[zmienna] = str(b/a)
		else:
			print("Podane kurwy nie sa liczbami.")
		return
	#label
	inp = re.search("([^\n \t]+) [Tt][Uu] [Bb][Yy][Ll]",line)
	if inp is not None:
		zmienna = str(inp.group(1))
		labele[zmienna] = i
		return
	inp = re.search("#([^\n \t]+)",line)
	if inp is not None:
		zmienna = str(inp.group(1))
		labele[zmienna] = i
		return
	#pojedynczy if
	inp = re.search("[Jj][Ee][Ss][Ll][Ii] ([^\n]+) [Zz][Aa][Pp][Ii][Ee][Rr][Dd][Aa][Ll][Aa][Jj] [Dd][Oo] ([^\n \t]+)",line)
	if inp is not None:
		exp = inp.group(1)
		zmienna = inp.group(2)
		if evaluate(exp):
			i = labele[zmienna]
		return
	#skacz
	inp = re.search("[Zz][Aa][Pp][Ii][Ee][Rr][Dd][Aa][Ll][Aa][Jj] [Dd][Oo] ([^\n \t]+)",line)
	if inp is not None:
		zmienna = str(inp.group(1))
		i = labele[zmienna]-1
		return
	#quit
	inp = re.search("[Ww][Yy][Pp][Ii][Ee][Rr][Dd][Aa][Ll][Aa][Jj] [Zz] [Oo][Kk][Rr][Zz][Yy][Kk][Ii][Ee][Mm] ([^\n]+)",line)
	if inp is not None:
		zmienna = inp.group(1)
		print(zmienna)
		quit()
	inp = re.search("[Ww][Yy][Pp][Ii][Ee][Rr][Dd][Aa][Ll][Aa][Jj]",line)
	if inp is not None:
		quit()

#mainloop
while(i<len(kod)-1):
	i = i + 1
	line = kod[i]
	if(debug):
		print(i)
	expression(line)

