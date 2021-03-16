f = open("datenday1", "r")
listItems = f.read().splitlines()
array_len = len(listItems)

var = 0
for x1 in range(array_len):
    if var == 1:
        break
    zahl1 = listItems[x1]
    for x2 in range(array_len):
        zahl2 = listItems[x2]
        if (int(zahl1) + int(zahl2)) == 2020:
            erg = int(zahl1) * int(zahl2)
            var = 1
            break

print(zahl1, zahl2)
print(erg)

f = open("datenday1", "r")
listItems = f.read().splitlines()
array_len = len(listItems)

#var = 0
#for x1 in range(array_len):
#    if var == 1:
#        break
#    zahl1 = listItems[x1]
#    for x2 in range(array_len):
#        if var == 1:
#            break
#        zahl2 = listItems[x2]
#        for x3 in range(array_len):
#            zahl3 = listItems[x3]
#            if (int(zahl1) + int(zahl2) + int(zahl3)) == 2020:
#                erg = int(zahl1) * int(zahl2) * int(zahl3)
#                var = 1
#                break
#
#print(zahl1, zahl2, zahl3)
#print(erg)
