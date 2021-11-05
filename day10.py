f = open("datenday10", "r")
listItems = f.read().split("\n")
array_len = len(listItems)

listItems= list(map(int, listItems))
listItems.append(0)
listItems.sort()
listItems.append(listItems[len(listItems) - 1] + 3)
print(listItems)

print(range(3-1, -1, -1))




# ------ PART ONE ------
#count_1, count_3 = 1, 1
#
#for i in range(len(listItems)):
#    try:
#        dif = listItems[i+1] - listItems[i]
#        if dif == 1:
#            count_1 +=1
#
#        else:
#            count_3 +=1
#
#    except IndexError:
#        break
#
#erg = count_1 * count_3
#print("1 jolt: ", count_1,"3 jolt: ", count_3, "\nErgebnis: ", erg)