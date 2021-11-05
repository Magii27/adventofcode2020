f = open("datenday9", "r")
listItems = f.read().split("\n")
array_len = len(listItems)
print(listItems)


def check_sum(data, number):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if sum(data[i:j+1]) == number:
                output = max(data[i:j+1]) + min(data[i:j+1])
                return output
    return False


number = 1639024365
listItems = list(map(int, listItems))

output = check_sum(listItems, number)
print(output)


# ------- PART ONE ------ #
#def check_sum(data, number):
#    for i in range(len(data)):
#        for j in range(i+1, len(data)):
#            if data[i] + data[j] == number:
#                return True
#    return False
#
#
#listItems = list(map(int, listItems))
#preamble = 25
#
#for num in range(preamble + 1, len(listItems)):
#   if not check_sum(listItems[num - preamble:num], listItems[num]):
#        print("Liste: ", listItems[num - preamble:num], "\nNummer: ", listItems[num])
#        break