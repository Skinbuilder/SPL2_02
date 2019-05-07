# variable.py

a=10
b=20
c=30

print(a+b+c)
print("Summe: ", a+b+c)

print ("Multipliaktion: ",a*b)

print ("Division: ",a/b)

print("Potenz: ",a**b)

text = "Hallo Welt"
print(text)
print(text * 2)

name = "Hannes Diewald"
print("Hallo" , name)

for i in ("Franz", "Karl", "Klaus"):
	print (i)
	
for i in (-4, 12, 32, 9, 0, -32, 654):
	print (i, end=" ")
	
for i in range(1, 100):
	print (i, end=".")
	
while (True):
	i *= 2
	print (i, end=".")