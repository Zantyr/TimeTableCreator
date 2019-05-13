#inicjalizacja
import urllib
import re
from time import sleep
settings = "settings.txt"
with open(settings) as file:
	for line in file:
		exec(line)
tbc = False
niewgranych = 0
with open(save) as file:
	for line in file:
		exec(line)
version = 1.3
eurodown = False
tryagain = True

#sprawdzenie wersji
conn = urllib.urlopen("http://arioch.pl/ONG/version.php")
content = conn.read()
i = re.findall("[0-9]+.[0-9]+", content)
check = float(i[0])
if(check!=version):
	print("\n")
	print(content)
	conn = urllib.urlopen("http://arioch.pl/ONG/current.php")
	content = conn.read()
	with open("complete.py", "w") as file:
		file.write(content)
	print("\nProgram zostal zaktualizowany. Uruchom go ponownie\n")
	quit()
else:
	print("Aktualna wersja: " + str(version))


#definicja klasy karta
class Karta:
	def __init__(self, nazwa="Karta", mset="Set", code="MSET-1", price=100.00):
		self.nazwa = nazwa
		self.set = mset
		self.code = code
		self.price = price

#kontynuacja
if(tbc):
	answer = ""
	while(not (answer=="tak" or answer=="nie" or answer=="koniec")):	
		answer = raw_input("Poprzednio zostalo kilka kart do wrzucenia(" + str(niewgranych) + "). Czy kontynuowac poprzednia sesje? (tak/nie/koniec) ")
		if(answer == "tak"):
			download = False
			rload = False
			upload = True
			eof = log
			ask = False
		if(answer == "koniec"):
			quit()

#zapytaj uzytkownika co zrobic
if(ask):
	answer = ""
	while(not (answer=="tak" or answer=="nie" or answer=="koniec")):	
		answer = raw_input("Czy sciagnac ceny? (tak/nie/koniec) ")
		if(answer == "tak"):
			download = True
			answer = ""
			while(not (answer=="tak" or answer=="nie" or answer=="koniec")):	
				answer = raw_input("Czy ponownie przeczytac liste kart? (tak/nie/koniec) ")
				if(answer == "tak"):
					rload = True
				if(answer == "nie"):
					rload = False
				if(answer == "koniec"):
					quit()
		if(answer == "nie"):
			download = False
		if(answer == "koniec"):
			quit()
	answer = ""
	while(not (answer=="tak" or answer=="nie" or answer=="koniec")):	
		answer = raw_input("Czy wgrywac ceny? (tak/nie/koniec) ")
		if(answer == "tak"):
			upload = True
		if(answer == "nie"):
			upload = False
		if(answer == "koniec"):
			quit()
	answer = ""

#no action chosen
if(not download and not upload):
	print("Nie wybrano zadnego dzialania, zakonczono dzialanie programu...")
	quit()

#import upload
if(upload):
	from selenium import webdriver
	from selenium.webdriver.common.by import By
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.support.ui import Select
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.common.exceptions import ElementNotVisibleException 
	from selenium.common.exceptions import TimeoutException
	from selenium.common.exceptions import StaleElementReferenceException


#przeladowanie spoilerlisty do pliku iof
if(download and rload):
	stringi = []
	with open(magicdb) as file:
		line = file.read()
		line = line + "\n\n"
		lista = re.findall("(\n)*([^\n]*)\n([^\n]+\n)+((([A-Z0-9]+-[CURM])+[, ]*)+)(\n)+", line)	
		for listaitem in lista:
			nazwen = listaitem[1]
			sets = listaitem[3]
			druga = re.findall("[A-Z]{3}-[CURM]", sets)
			for item in druga:
				mset = item[:3]
				rarity = item[4]
				if mset=="ORI":
					mset="Magic Origins"
					stringi.append(nazwen + "%" + mset + "%" + rarity + "%0.00%\n")
					continue
				if mset=="BFZ":
					mset="Battle for Zendikar"
					stringi.append(nazwen + "%" + mset + "%" + rarity + "%0.00%\n")
					continue
				if mset=="KTK":
					mset="Khans of Tarkir"
					stringi.append(nazwen + "%" + mset + "%" + rarity + "%0.00%\n")
					continue
				if mset=="FRF":
					mset="Fate Reforged"
					stringi.append(nazwen + "%" + mset + "%" + rarity + "%0.00%\n")
					continue
				if mset=="DTK":
					mset="Dragons of Tarkir"
					stringi.append(nazwen + "%" + mset + "%" + rarity + "%0.00%\n")
					continue
	with open(iof, "w") as file:
		for string in stringi:
			file.write(string)
	print("Przeczytano baze danych, liczba wejsc: " + str(len(stringi)))

#pobranie kursu Euro
if(eurodown):
	conn = urllib.urlopen("http://www.nbp.pl/home.aspx?f=%2Fkursy%2Fkursyc.html")
	content = conn.read()
	pattern = "EUR</td> <td class=\"bgt2 right\">[0-9,]*</td> <td class=\"bgt2 right\">[0-9,]*</td>"
	inputs = re.findall(pattern, content)
	for i in inputs:
		korwin = re.findall("[0-9]*,[0-9]*", i)
		i = korwin[1]
		i = i.replace(",", ".")	
		kurs = float(i)
	print("Kurs EUR: " + str(kurs))
else:
	i = raw_input("Podaj kurs Euro: ")
	i = i.replace(",", ".")	
	kurs = float(i)

#wczytaj dane z pliku iof do listy karty[]
if(download):
	karty = []
	iterator = 0
	with open(iof) as iofile:
		for line in iofile:
			iolist = re.findall("[^\n%]*%", line)
			karta = Karta()
			iterator						
			for item in iolist:
				korwin = re.search("%", item)
				item = item[:korwin.start()]
				if iterator == 0:
					karta.nazwa = item
				if iterator == 1:
					karta.set = item
				if iterator == 2:
					karta.code = item
				if iterator == 3:
					item = item.replace(",",".")
					karta.price = kurs * float(item)		
				iterator = iterator + 1
				if iterator>3:
					iterator = 0
			karty.append(karta)
	print("Wczytano karty z pliku do db")


#dla listy karty[] pobierz ceny i zapisz w eof
if(download):
	counter = 0
	with open(eof, "w") as file:
		for karta in karty:
			urlnazwa = urllib.quote_plus(karta.nazwa)
			urlset = urllib.quote_plus(karta.set)
			urlkarty = "https://www.magiccardmarket.eu/Products/Singles/" + urlset + "/" + urlnazwa
			conn = urllib.urlopen(urlkarty)
			content = conn.read()
			korwin = re.search("Price Trend[^\n]*\>(\d+[\.,]\d{2})[^\n]*Available", content)

			if korwin is not None:

				kurw = korwin.group(1)
				kurw = kurw.replace(",",".")
				cena = float(kurw)
				karta.price = kurs * cena
				if karta.code=="C":
					if karta.price<Cmin:
						karta.price = Cmin
				if karta.code=="U":
					if karta.price<Umin:
						karta.price = Umin
				if karta.code=="R":
					if karta.price<Rmin:
						karta.price = Rmin
				if karta.code=="M":
					if karta.price<Mmin:
						karta.price = Mmin				
				file.write(karta.nazwa + "%")
				file.write(karta.set + "%" + karta.code + "%")
				file.write("%.2f" % karta.price + "%\n")
				counter = counter + 1
				print("Pobrano cene karty: " + str(counter))
	print("Ukonczono pobieranie")

#jesli nie pobierasz cen, wczytaj je z eof[]
if(upload and not download):
	karty = []
	iterator = 0
	with open(eof) as iofile:
		for line in iofile:
			iolist = re.findall("[^\n%]*%", line)
			karta = Karta()
			iterator						
			for item in iolist:
				korwin = re.search("%", item)
				item = item[:korwin.start()]
				if iterator == 0:
					karta.nazwa = item
				if iterator == 1:
					karta.set = item
				if iterator == 2:
					karta.code = item
				if iterator == 3:
					item = item.replace(",",".")
					karta.price = float(item)		
				iterator = iterator + 1
				if iterator>3:
					iterator = 0
			karty.append(karta)
	print("Wczytano karty z pliku do bazy danych")

#zaloguj i przejdz do katalogu
if(upload):
	driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
	driver.get(address)
	wait = WebDriverWait(driver, 10)
	elem = wait.until(EC.element_to_be_clickable((By.NAME,'email')))	
	elem.send_keys(email)
	wait = WebDriverWait(driver, 10)
	elem = wait.until(EC.element_to_be_clickable((By.NAME,'passwd')))	
	elem.send_keys(haslo)
	elem.send_keys(Keys.RETURN)
	wait = WebDriverWait(driver, 10)
	elem = wait.until(EC.element_to_be_clickable((By.ID,'maintab-AdminCatalog')))	
	elem.click()
	wait = WebDriverWait(driver, 10)
	elem = wait.until(EC.element_to_be_clickable((By.NAME,'productFilter_b!name')))

#wstaw wszystkie przedmioty z listy karty[]
if(upload):
	kartynotdone = []
	zeroprice = []
	for karta in karty:
		if(karta.price != 0.0):
			try:
				elem.clear()
				nameRe = re.match("([^\n/]*) /", karta.nazwa)
				if(nameRe is not None):
					karta.nazwa = nameRe.group(1)
				elem.send_keys(karta.nazwa)
				if(elem.get_attribute('value') == ""):
					sleep(smallsleep)
					elem.send_keys(karta.nazwa)
				wait = WebDriverWait(driver, 10)
				elem = wait.until(EC.element_to_be_clickable((By.NAME,'productFilter_cl!name')))
				elem.clear()
				elem.send_keys(karta.set)
				if(elem.get_attribute('value') == ""):
					sleep(smallsleep)
					elem.send_keys(karta.set)
				elem.send_keys(Keys.RETURN)
				wait = WebDriverWait(driver, 10)
				elem = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Edit')))
				elem.click()
				wait = WebDriverWait(driver, 10)
				elem = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Prices')))
				elem.click()

				wait = WebDriverWait(driver, 10)
				elem = Select(wait.until(EC.element_to_be_clickable((By.ID,'id_tax_rules_group'))))
				elem.select_by_value('53')	

				wait = WebDriverWait(driver, 10)
				elem = wait.until(EC.element_to_be_clickable((By.ID,'priceTI')))	
				elem.clear()
				elem.send_keys(str(karta.price))
				if(elem.get_attribute('value') == ""):
					sleep(smallsleep)
					elem.send_keys(str(karta.price))
				elem.send_keys(Keys.RETURN)
				sleep(normalsleep)
				elem = driver.find_element_by_name("submitAddproduct")	
				driver.execute_script("var x = document.getElementsByName(\"submitAddproduct\"); x[0].click();")
				wait = WebDriverWait(driver, 10)
				elem = wait.until(EC.element_to_be_clickable((By.NAME,'productFilter_b!name')))
			except TimeoutException:
				try:			
					wait = WebDriverWait(driver, 10)
					elem = wait.until(EC.element_to_be_clickable((By.ID,'maintab-AdminCatalog')))	
					elem.click()
					wait = WebDriverWait(driver, 10)
					elem = wait.until(EC.element_to_be_clickable((By.NAME,'productFilter_b!name')))
					kartynotdone.append(karta)
				except TimeoutException:
					kartynotdone.append(karta)
			except StaleElementReferenceException:
				try:			
					wait = WebDriverWait(driver, 10)
					elem = wait.until(EC.element_to_be_clickable((By.ID,'maintab-AdminCatalog')))	
					elem.click()
					wait = WebDriverWait(driver, 10)
					elem = wait.until(EC.element_to_be_clickable((By.NAME,'productFilter_b!name')))
					kartynotdone.append(karta)
				except TimeoutException:
					kartynotdone.append(karta)
		else:
			zeroprice.append(karta)		
	
if(tryagain and upload and len(zeroprice)):
	counter = 0
	print("Ilosc kart z zerowa cena: " + str(len(zeroprice)))
	for karta in zeroprice:
		urlnazwa = urllib.quote_plus(karta.nazwa)
		urlset = urllib.quote_plus(karta.set)
		urlkarty = "https://www.magiccardmarket.eu/Products/Singles/" + urlset + "/" + urlnazwa
		conn = urllib.urlopen(urlkarty)
		content = conn.read()
		korwin = re.search("Price Trend[^\n]*\>(\d+[\.,]\d{2})[^\n]*Available", content)

		if korwin is not None:
			kurw = korwin.group(1)
			kurw = kurw.replace(",",".")
			cena = float(kurw)
			karta.price = kurs * cena
			if karta.code=="C":
				if karta.price<Cmin:
					karta.price = Cmin
			if karta.code=="U":
				if karta.price<Umin:
					karta.price = Umin
			if karta.code=="R":
				if karta.price<Rmin:
					karta.price = Rmin
			if karta.code=="M":
				if karta.price<Mmin:
					karta.price = Mmin				
			counter = counter + 1
			print("Pobrano ponownie cene karty: " + str(counter))
		kartynotdone.append(karta)
	print("Ukonczono ponowne pobieranie cen")
	driver.get(address)
	wait = WebDriverWait(driver, 10)
	elem = wait.until(EC.element_to_be_clickable((By.NAME,'email')))	
	elem.send_keys(email)
	wait = WebDriverWait(driver, 10)
	elem = wait.until(EC.element_to_be_clickable((By.NAME,'passwd')))	
	elem.send_keys(haslo)
	elem.send_keys(Keys.RETURN)
	wait = WebDriverWait(driver, 10)
	elem = wait.until(EC.element_to_be_clickable((By.ID,'maintab-AdminCatalog')))	
	elem.click()
	wait = WebDriverWait(driver, 10)
	elem = wait.until(EC.element_to_be_clickable((By.NAME,'productFilter_b!name')))

if(tryagain and upload and len(kartynotdone)):
	print("Ponowne wrzucanie kart niewrzuconych. Ilosc kart: " + str(len(kartynotdone)))
	karty = kartynotdone
	kartynotdone = []
	for karta in karty:
		if(karta.price != 0.0):
			try:
				elem.clear()
				nameRe = re.match("([^\n/]*) /", karta.nazwa)
				if(nameRe is not None):
					karta.nazwa = nameRe.group(1)
				elem.send_keys(karta.nazwa)
				if(elem.get_attribute('value') == ""):
					sleep(smallsleep)
					elem.send_keys(karta.nazwa)
				wait = WebDriverWait(driver, 10)
				elem = wait.until(EC.element_to_be_clickable((By.NAME,'productFilter_cl!name')))
				elem.clear()
				elem.send_keys(karta.set)
				if(elem.get_attribute('value') == ""):
					sleep(smallsleep)
					elem.send_keys(karta.set)
				elem.send_keys(Keys.RETURN)
				wait = WebDriverWait(driver, 10)
				elem = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Edit')))
				elem.click()
				wait = WebDriverWait(driver, 10)
				elem = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Prices')))
				elem.click()

				wait = WebDriverWait(driver, 10)
				elem = Select(wait.until(EC.element_to_be_clickable((By.ID,'id_tax_rules_group'))))
				elem.select_by_value('53')	

				wait = WebDriverWait(driver, 10)
				elem = wait.until(EC.element_to_be_clickable((By.ID,'priceTI')))	
				elem.clear()
				elem.send_keys(str(karta.price))
				if(elem.get_attribute('value') == ""):
					sleep(smallsleep)
					elem.send_keys(str(karta.price))
				elem.send_keys(Keys.RETURN)
				sleep(normalsleep)
				elem = driver.find_element_by_name("submitAddproduct")	
				driver.execute_script("var x = document.getElementsByName(\"submitAddproduct\"); x[0].click();")
				wait = WebDriverWait(driver, 10)
				elem = wait.until(EC.element_to_be_clickable((By.NAME,'productFilter_b!name')))
			except TimeoutException:
				try:			
					wait = WebDriverWait(driver, 10)
					elem = wait.until(EC.element_to_be_clickable((By.ID,'maintab-AdminCatalog')))	
					elem.click()
					wait = WebDriverWait(driver, 10)
					elem = wait.until(EC.element_to_be_clickable((By.NAME,'productFilter_b!name')))
					kartynotdone.append(karta)
				except TimeoutException:
					kartynotdone.append(karta)
			except StaleElementReferenceException:
				try:			
					wait = WebDriverWait(driver, 10)
					elem = wait.until(EC.element_to_be_clickable((By.ID,'maintab-AdminCatalog')))	
					elem.click()
					wait = WebDriverWait(driver, 10)
					elem = wait.until(EC.element_to_be_clickable((By.NAME,'productFilter_b!name')))
					kartynotdone.append(karta)
				except TimeoutException:
					kartynotdone.append(karta)
		else:
			kartynotdone.append(karta)

#Zgranie kart niewgranych do sklepu
if(upload):
	gottasave = False
	with open(log, "w") as file:
		for karta in kartynotdone:
			if(karta.nazwa != "Karta"):
				print("Karta o nazwie " + karta.nazwa + " nie zostala zaktualizowana.")
				file.write(karta.nazwa + "%")
				file.write(karta.set + "%" + karta.code + "%")
				file.write("%.2f" % karta.price + "%\n")
				gottasave = True
	with open(save, "w") as file:
		if(gottasave):
			file.write("tbc = True\n")
			file.write("niewgranych = " + str(len(kartynotdone)) + "\n")
		else:
			file.write("tbc = False\n")
			print("Wszystkie karty zostaly wgrane")
			
#Zakonczenie procesu
print("Process complete")
sleep(grandsleep)
if(upload):
	driver.close()
