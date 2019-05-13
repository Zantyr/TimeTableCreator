global obecnypakoj
obecnypakoj = 0
def TRIGGER(trigger=0):
	global obecnypakoj	
	if trigger==0:
		return
	if trigger==1:
		print "przejebales"
		quit()
	if trigger==2:
		obecnypakoj = 1
		print PAKOJE[obecnypakoj].opis		
	return

class Pokuj:
	def __init__ (self, opis="PustyPokuj"):
		self.opis=opis
		self.odpowiedzi={}
		self.trigger={}
	def dodajinterakcje(self,komenda="wypierdol", odpowiedz="matke Czouga", trigger=0):
		self.odpowiedzi[komenda] = odpowiedz
		self.trigger[komenda] = trigger
	def interakcje(self,komenda):
		if komenda in self.odpowiedzi.keys():
			print self.odpowiedzi[komenda]
			TRIGGER(self.trigger[komenda])
		else:
			print "Nie ma takiej kurwa komendy"

PAKOJE = []
tymczasowypakoj = Pokuj("Ten pokoj to kurwa stary grat.")
tymczasowypakoj.dodajinterakcje("sraj", "srasz na podloge", 1)
tymczasowypakoj.dodajinterakcje("idz w pizdu", "idziesz w pizdu", 2)
PAKOJE.append(tymczasowypakoj)
tymczasowypakoj = Pokuj("Widzisz sciany pizdy. To matka Czouga.")
tymczasowypakoj.dodajinterakcje("sraj", "srasz na podloge", 1)
tymczasowypakoj.dodajinterakcje("ruchaj","Chcesz ruchac matke czouga? Pojebawszy?",0)
tymczasowypakoj.dodajinterakcje("why", "chciales wejsc w lochy", 0)
tymczasowypakoj.dodajinterakcje()
PAKOJE.append(tymczasowypakoj)
print '>So who are you again, bitch?'
name = raw_input()
fame = 69
balans = 100
rur = 0
slownikkontrolny = {}
if name != "Saito" and name != "Zantyr":	
	print '>Dzien dobry ' + name
	print '>Ten program jest dostepny tylko dla kurwia.'
	quit()
print '>Witaj kurwiu'
print '>Oto Twoje Krulestwo. Sklada sie z zejscia do podziemi, rurkowca i Krulestwa wlasciwego. Co chcesz uczynic?'
#Start programu
slownikkontrolny["ruchaczforeva"] = False	
while(not slownikkontrolny["ruchaczforeva"]):
	command = raw_input()
	if command == "help" or command == "pomoc":
		print ">Dostepne komendy to:"
		print ">balans, poparcie, wyjdz, walcz. Jestes frajerem, skoro ich nie znasz."
	if command == "balans":
		print ">W tej chwili w skarbcu znajduje sie " + str(balans) + " milionuw sztuk zlota."
	if command == "poparcie":
		print ">Na ten moment popiera Cie " + str(fame) + "% spoleczenstwa."
	if command == "wyjdz":
		print ">Wychodzimy kurwa."
		quit()
	if command == "walcz":
		print ">Atakuje Cie wsciekly rurkowiec!"
		print "Co zechcesz uczynic?"
		xD = raw_input()
		if xD == "wpierdol":
			print ">Twoj hit zadaje 360 damage do rurkowca."
			print ">Rurkowiec nie zyje."
			print ">Zdobywasz 420 xp"
			rur+=420
			print ">Masz na ten moment " + str(rur) + "doswiadczenia."
		else:
			print ">Rurkowiec atakuje."
			print ">Rurkowiec zadaje 1 dmg"
			print ">Niestety jestes ciota i rurkowiec Cie zabil"
			print ">Cioto"
			quit()
	if command == "zejdz w podziemie":
		slownikkontrolny["ruchaczforeva"] = True
print ">Wybierz poziom trudnosci (HINT: superkurwahard)"
command = raw_input()
if command != "superkurwahard":
	print ">Niestety nie ma takiego poziomu trudnosci. Wypierdalaj."
	quit()
print ">Get redi to get rekt u scrub"
hp = 5
lvl = 1
sil = 1
zre = 1
moc = 1
help = ">Dostepne komendy to: idz, patrz, bij, ksiega, czaruj, eq, status."
print ">Schodzisz ciemnymi schodami powoli zapominajac kim jestes i co sie z Toba dzialo..."
if name == "Saito":
	print "...to byla gruba impreza ruchaczu foreva. Obok lezy cialo martwej dziewicy z rozprutym lonem."
print ">W koncu sie zatrzymujesz. Kim jestes? Nie pamietasz nic. Przed Toba korytarz, za Toba sciana."
print "UWAGA: Literowke mozna popelnic tylko raz, wiec uwazaj, by nie wyjebalo Cie z programu. Pisz help po komendy."
zmiennawyjscia = True
while(zmiennawyjscia):
	czyn = raw_input()
	if czyn == "help":
		print help
		continue
	if czyn == "patrz":
		print PAKOJE[obecnypakoj].opis
		continue
	if czyn == "eq":
		print ">Masz na sobie tylko brudne szmaty."
		continue
	if czyn == "bij":
		print ">Nie ma kogo"
		continue
	if czyn == "bij matke Czouga":
		print ">Bijesz matke Czouga swoim kutasem"
		continue
	if czyn == "ksiega":
		print ">Nie masz ksiegi zaklec."
		continue
	if czyn == "czaruj":
		print ">Nie znasz zadnych zaklec."
		continue
	if czyn == "status":
		print ">Na ten moment masz:"
		print ">" + str(sil) + " sily, co przeklada sie na " + str(5*sil) + " max hp."
		print ">" + str(zre) + " zrecznosci."
		print ">" + str(moc) + " inteligencji."
		print ">" + str(hp) + " punktow wytrzymalosci."
		print ">" + str(lvl) + " poziom."
		continue
	PAKOJE[obecnypakoj].interakcje(czyn)

