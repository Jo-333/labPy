
#esercizio sulle stringhe

stringa = input('Inserisci una stringa: ')

print(stringa)

lettere = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','y','z']

i=0

print("ciclo while")
while i < len(stringa):
    print(stringa[i], " ", ord(stringa[i]))
    i = i + 1


for elemento in lettere:
    print(elemento)


Conteggio = 0
for Carattere in stringa:
  if Carattere == 'a':
    Conteggio = Conteggio + 1
print (Conteggio)

