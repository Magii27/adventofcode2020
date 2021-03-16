f = open("datenday3", "r")
listItems = f.read().splitlines()
array_len = len(listItems)

print(listItems)
var = 1
erg = 1
while var == 1:
    right = int(input("how many right: \n"))
    down = int(input("how many down: \n"))
    last = 0
    lastdown = 0
    countertree = 0
    countersq = 0

    for x in range(array_len):
        try:
            if last >= (len(listItems[lastdown]) - right):
                last = last - len(listItems[lastdown])
            lastdown += down
            num = listItems[lastdown]
            postest = num[:last + right] + "X" + num[last + right + 1:]
            pos = num[last + right:last + right + 1]

            if pos == "#":
                countertree += 1
                postest = num[:last + right] + "X" + num[last + right + 1:]
            else:
                countersq += 1
                postest = num[:last + right] + "O" + num[last + right + 1:]
            print(postest, pos)
            last += right
        except IndexError:
            break
    erg = erg * countertree
    print("Trees: ", countertree)
    print("Squares: ", countersq)
    print("zwischen: ", erg)
    var1 = input("weiter?")
    if var1 == "e":
        var = 0


print(erg)

