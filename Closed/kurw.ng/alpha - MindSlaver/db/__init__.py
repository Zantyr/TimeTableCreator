print "Loading the DB package..."

global mainDB, DBs
mainDB = "DB/main.db"
DBfiles = []
DBs = []

def listDB():
	global DBfiles, mainDB
	with open(mainDB, "r") as f:
		for line in f:
			DBfiles.append(f.readline())
	return

def loadDB(DBname="DB.csv",separator="	"):
	DB = {}
	with open(DBname, "r") as f:
		l = f.readline()
		struct = l.split(separator)
		for line in f[1:]:
			l = f.readline()
			rec = l.split(separator)
			DB[rec[0]] = rec[1:]
	return (struct, DB)

def saveDB(DBname="DB.csv",separator="	"):
	with open(DBname, "w") as f:
		f.write(separator.join(struct))
		for line in list(DB):
			f.write(separator.join(([line[0]]+line[1])))
	return

def addDB(DB, record):
	return

def editDB(DB, ID, record):
	return

def removeDB(DB, ID):
	return

def readDB(DB, ID):
	global DBs
	return DBs[DB][1][ID]

def search(DB, variable, varvalue):
	searchedList,index = [],0
	for e,i in enumerate(DBs[DB][0]):
		if i == variable:
			index = e+1
	if not index: return None
	for i in DBs[DB][1]:
		if i[index] == varvalue: searchedList.append(i)
	return searchedList
