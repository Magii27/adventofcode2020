f = open("datenday7", "r")
listItems = f.read().split("\n")
array_len = len(listItems)
print(listItems)

bags = []
erg = 0
erg1 = 0
for x in listItems:
    if "shiny gold" in x[x.find(" "):]:
        if x[0:x.find(" ") + 1 + x[x.find(" ") + 1:].find(" ")] not in bags:
            bags.append(x[0:x.find(" ") + 1 + x[x.find(" ") + 1:].find(" ")])
            erg += 1

while erg != erg1:
    erg1 = erg
    for x in listItems:
        for x1 in bags:
            if x1 in x[x.find(" ") + 1 + x[x.find(" ") + 1:].find(" "):]:
                if x[0:x.find(" ") + 1 + x[x.find(" ") + 1:].find(" ")] not in bags:
                    erg += 1
                    bags.append(x[0:x.find(" ") + 1 + x[x.find(" ") + 1:].find(" ")])
print(erg)