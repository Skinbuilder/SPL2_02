# primes.py
# erzeugen der Primzahlen von 1 bis 1000
#Achtung 1 ist per Definition keine Primzahlen

i = 1
x = 0

for i in range (1,1000):
	for x in range(1, i):
		if(i%x == 0):
			print(i)