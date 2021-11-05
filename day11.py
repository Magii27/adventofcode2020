f = open("datenday11", "r")
listItems = f.read().split("\n")
array_len = len(listItems)
print(listItems)

temp = listItems

for x in range(len(listItems)):
    for y in range(len(listItems[x])):
        if listItems[x][y] == ".":
            continue
        elif listItems[x][y] == "L":
            if x != 0 and x != len(listItems):
                if y != 0 and y != len(listItems[x]):
                    for n1 in range(0, 2):
                        for n in range(-1, 1):
                            if n1 == 0:
                                if listItems[x][y + 1] or listItems[x][y - 1] or :
                                    break
                                elif listItems[x][y - 1] == "#":
                        else:
                            continue

                        break
