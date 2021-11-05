f = open("datenday5", "r")
listItems = f.read().splitlines()
array_len = len(listItems)
print(listItems)
print(array_len)
z = 0
bigseatid = 0
seatid = 0
seats = []
for x in listItems:
    n = 128
    n2 = 8
    p = 0
    zw = 0
    zwc = 0
    zws = 0
    zwe = 127
    zwcs = 0
    zwce = 7
    for x1 in x:
        print(x)
        if x[p:p + 1] == "B":
            n = n / 2
            zws = zws + n
            print("start: ", zws, "Ende: ", zwe)
        elif x[p:p + 1] == "F":
            n = n / 2
            zwe = zwe - n
            print("start: ", zws, "Ende: ", zwe)
        elif zws == zwe:
            zw = zws
            print(zw)
            if x[p:p + 1] == "R":
                n2 = n2 / 2
                zwcs = zwcs + n2
                print("ZEILE start: ", zwcs, "Ende: ", zwce)
            elif x[p:p + 1] == "L":
                n2 = n2 / 2
                zwce = zwce - n2
                print("ZEILE start: ", zwcs, "Ende: ", zwce)

            zwc = zwcs
            print("test zwc", zwc)
            print("test zw", zw)
            print("aktuelle seatid:", seatid)
            print("größte seatid", bigseatid)
        p += 1
    z += 1
    seatid = zw * 8 + zwc
    if bigseatid < seatid:
        bigseatid = seatid
    seats.append(seatid)

seats.sort()
na = []
zahl1 = 100
for x in seats:
    if x != zahl1:
        na.append(zahl1)
        zahl1 +=1
    zahl1 +=1
    print("seat", x)
    print(na)








#zw = zwe - zws
#n = 128
#n = n / 2
#f -> zwe = zwe - n
#b -> zws = zws + n