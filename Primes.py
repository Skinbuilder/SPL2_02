# primes.py
# erzeugen der Primzahlen von 1 bis 1000
#Achtung 1 ist per Definition keine Primzahlen



for i in range (2,1001):
	Primzahl = True
	for x in range(2, i):
		if(i%x == 0):
			Primzahl = False
			break
	if(Primzahl == True):
		print(i)
	
			