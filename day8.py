f = open("datenday8", "r")
listItems = f.read().split("\n")
array_len = len(listItems)
print(listItems)

def operation(value, num, row):
    value_instruction = value[:value.find(" ")]
    value_number = int(value[value.find(" ") + 1:])
    if value_instruction == "nop":
        row += 1
        return num, row
    elif value_instruction == "acc":
        num += value_number
        row += 1
        return num, row
    elif value_instruction == "jmp":
        row += value_number
        return num, row

z = 0
for x in listItems:
    if x[:x.find(" ")] == "nop":
        print("found nop: " + listItems[z])
        value_saved = x
        listItems[z] = "jmp " + value_saved[x.find(" ") + 1:]
        print("Changed it to: " + listItems[z])
        dict = []
        num = 0
        row = 0
        while True:
            try:
                if row in dict:
                    break
                dict.append(row)
                num, row = operation(listItems[row], num, row)
            except IndexError:
                print("hier1")
                break
        listItems[z] = value_saved
        print("num: " + str(num), "row: " + str(row))
    elif x[:x.find(" ")] == "jmp":
        print("found jmp: " + listItems[z])
        value_saved = x
        listItems[z] = "nop " + value_saved[x.find(" ") + 1:]
        print("Changed it to: " + listItems[z])
        dict = []
        num = 0
        row = 0
        while True:
            try:
                if row in dict:
                    break
                dict.append(row)
                num, row = operation(listItems[row], num, row)
            except IndexError:
                print("hier2")
                break
        print("num: " + str(num), "row: " + str(row))
    z += 1

#dict = []
#num = 0
#row = 0
#while True:
#    row1 = row
#    num1 = num
#    if row in dict:
#        test = listItems[row1]
#        if listItems[row1][:test.find(" ")] == "nop":
#            test = "jmp " + listItems[row1][listItems[row1].find(" ") + 1:]
#
#            print("dict1: " + str(dict), "num: " + str(num), "row: " + str(row))
#            num, row = operation(test, num1, row1)
#            continue
#        else:
#            test = "nop " + listItems[row1][listItems[row1].find(" ") + 1:]
#            print("dict2: " + str(dict), "num: " + str(num), "row: " + str(row))
#            num, row = operation(test, num1, row1)
#
#            continue
#    dict.append(row)
#    num, row = operation(listItems[row], num, row)


#print("num: " + str(num), "row: " + str(row))


# -- PART ONE --

#dict = []
#num = 0
#row = 0
#while True:
#    if row in dict:
#        break
#    dict.append(row)
#    num, row = operation(listItems[row], num, row)
#
#print("num: " + str(num), "row: " + str(row))