#Elorap
#testin'
#Importin'
import csv
import random
from shutil import copyfile
#globalin'
global zero
global n
global name
global Usuw
#dictin'
zero = '0'
Usuw = []
Dict = {}
Keys = {}
List = []
#classin'
class klasa:
	ID = 0
	name = 'name'
#Functin'
# Funkcja Ladowanie
def load():
	global n
	with open('elorap.csv',"r") as f:
		reader = csv.reader(f,delimiter = ",")
		data = list(reader)
		row_count = len(data) 
	n = row_count
#Funkcja elorap
def zapisz():
	with open('elorap.csv', 'a') as csvfile:
		fieldnames = ['ID', 'name']
	  	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow({'ID': n, 'name':name})
	return
#funkcja reset
def reset():
	global n
	with open('elorap.csv', 'w') as csvfile:
		fieldnames = ['ID', 'name']
	  	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
	with open('elorap.csv',"r") as f:
		reader = csv.reader(f,delimiter = ",")
		data = list(reader)
		row_count = len(data) 
	n = row_count
#Funkcja szukaj
def szukaj(toBeFound):
	found = 0
	with open('elorap.csv', 'rt') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			for field in row:
				if field == toBeFound:
			      		print "Istnieje taki rekord."
					found = 1
	if found == 0:
		print "Nie ma takiego rekordu."
	return
#Funkcja usun
def usun():
	print 'Wpisz id rekordu do usuniecia'
	usuwane = raw_input()
	with open('elorap.csv', 'rb') as inp, open('backup/belorap.csv', 'wb') as out:
		writer = csv.writer(out)
		for row in csv.reader(inp):
			if row != usuwane:
				writer.writerow(row)
	copyfile('backup/belorap.csv','elorap.csv')
	load()
List.append(klasa)
print "Co chcesz uczynic kurwiu?(Press q to wypierdalaj.)"
load()
#Petlin'
while zero == '0':
	comm = raw_input('')
	if comm == 'q':
		quit()
	if comm == 'dodaj':
		#Zmienia lub dodaje rekord
		print 'Nazwij.'
		addwhat = raw_input('')
		name = addwhat
		Dict[addwhat] = klasa()
		Dict[addwhat].id = n
		Dict[addwhat].name = name
		List.append(Dict[addwhat])
		print "Gotowe."
		print "NAME:" + str(Dict[addwhat].name)
		print "AJDI:" + str(Dict[addwhat].id)
		zapisz()
		n = n+1
	if comm == 'all':
		#Wyswietla wszystkie istniejace rekordy
		if n == 0:
			print "Na ten moment mamy " + str(n) + " zmiennych."
		else:
			print "Na ten moment mamy " + str(n-1) + " zmiennych."
		stack = List
		with open('elorap.csv', 'rb') as f:
    			reader = csv.reader(f)
    			for row in reader:
        			print row
	if comm == 'ANDHISNAMEIS':
		foo = ['ANDRZEJ DUDA!', 'MARIAN KOWALSKI!', 'JOHN CENA!','ROBERT GIERCZAK!(dedicated dla czouga)','ZBIGNIEW STONOGA!']
		print(random.choice(foo))
	if comm == 'backup':
		print 'Inicjowanie backupu'
		copyfile('elorap.csv', 'backup/backup.csv')
		print 'Gotowe'
	if comm == 'load':
		print 'Ladowanie backupu'
		copyfile('backup/backup.csv','elorap.csv')
		load()
	if comm == 'reset':
		print 'Are you sure?(y/n)'
		sure = raw_input()
		if sure == 'y' or sure == 'Y':
			reset()
	if comm == 'szukaj':
		print 'Wpisz fraze do wyszukania'
		szukane = raw_input()
		szukaj(szukane)
	if comm == 'usun':
		usun()
