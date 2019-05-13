ADDR = " "
ADDRS = []
while ADDR:
	ADDR = raw_input("Podaj adres pliku: ")
	ADDRS.append(ADDR)
TO = raw_input("Podaj nazwe docelowa: ")
for ADDR in ADDRS:
	with open(ADDR,"r") as f:
		STR = f.read()
	NEW,dic,pre,post = "",{}, "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM", "djreglhvbcnfqstuwxymkpioazDJREGLHVBCNFQSTUWXYMKPIOAZ"
	for i in xrange(len(pre)):
		dic[pre[i]] = post[i]
	for i in STR:
		try:
			NEW += (dic[i])
		except KeyError:
			NEW += i
	with open(TO, "a") as f:
		f.write(ADDR+"\n"+NEW+"\n")
