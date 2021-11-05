p = 19441
q = 80141
N = 1558021181
e = 21
print("p=", p, "q=", q, "N=", N, "e=", e)
eingabe = 25928#int(input("Zu verschlüsseln: "))
print(eingabe)
ergebnis = int(eingabe**e % N)
print(str(eingabe) + "^" + str(e) + "%" + str(N) + "=" + str(ergebnis))


d = 109270 + 103519
entschlüsselung = ergebnis ** d % N
print(entschlüsselung)
p = 0
q = 0
primzahl = []

for x in range(1, 81000):
    for i in range(2, x):
        if (x % i) == 0:
            break
    else:
        primzahl.append(x)

while p * q != N:
    print("hi")
    for x in range(len(primzahl)):
        for i in range(len(primzahl)):
            if primzahl[x] * primzahl[i] == N:
                print("Ergebnis gefunden: p=" + str(primzahl[x]) + " q=" + str(primzahl[i]))
                p = primzahl[x]
                q = primzahl[i]
                break
        if primzahl[x] * primzahl[i] == N:
            break
#p = 98909
#q = 99103
#N = p * q
#e = 19
#print("p=", p, "q=", q, "N=", N, "e=", e)
#eingabe = 25928#int(input("Zu verschlüsseln: "))
#print(eingabe)
#ergebnis = int(eingabe**e % N)
#print(str(eingabe) + "^" + str(e) + "%" + str(N) + "=" + str(ergebnis))
##(d * e) % ((p-1)*(q-1)) = 1
##1*d + 1*31 % 336 = 1
##1 = d + 31 % 336
##1 - 31 = d %336
#d = 109270 + 103519
#entschlüsselung = ergebnis ** d % N
#print(entschlüsselung)
#p = 0
#q = 0
#primzahl = []
#for x in range(1, 100000):
#    for i in range(2, x):
#        if (x % i) == 0:
#            break
#    else:
#        primzahl.append(x)
#
#while p * q != N:
#    for x in range(len(primzahl)):
#        for i in range(len(primzahl)):
#            if primzahl[x] * primzahl[i] == N:
#                print("Ergebnis gefunden: p=" + str(primzahl[x]) + " q=" + str(primzahl[i]))
#                p = primzahl[x]
#                q = primzahl[i]
#                break
#        if primzahl[x] * primzahl[i] == N:
#            break