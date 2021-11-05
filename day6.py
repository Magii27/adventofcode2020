f = open("datenday6", "r")
listItems = f.read().split("\n\n")
listItems1 = []
for x in listItems:
    test = x.split("\n")
    listItems1.append(test)

listItems = listItems1
array_len = len(listItems)
print(listItems)

# -- PART TWO --

abc = []
num = 0
erg = 0
for x in listItems:
    pos = 0
    forbidden = []
    num = 0
    for x1 in x:
        #print(x.intersection(x))
        test = listItems[num]
        letter = x[pos:pos + 1]
        if letter == " ":
            erg +=0
        if letter == "\n":
            erg +=0
        elif letter in forbidden:
            erg +=0
        elif x.count(letter) > 1:
            forbidden.append(letter)
            erg +=1
        elif x.count(letter) == 1:
            erg +=1
        num =+1
        pos +=1
    num =+1
print(erg)


# -- PART ONE --

#f = open("datenday6", "r")
#listItems = f.read().split("\n\n")
#array_len = len(listItems)
#print(listItems)
#
#abc = []
#num = 0
#erg = 0
#for x in listItems:
#    pos = 0
#    forbidden = []
#    for x1 in x:
#        test = listItems[num]
#        letter = x[pos:pos + 1]
#        if letter == " ":
#            erg +=0
#        if letter == "\n":
#            erg +=0
#        elif letter in forbidden:
#            erg +=0
#        elif x.count(letter) > 1:
#            forbidden.append(letter)
#            erg +=1
#        elif x.count(letter) == 1:
#            erg +=1
#
#        pos +=1
#    num =+1
#print(erg)