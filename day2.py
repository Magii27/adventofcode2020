f = open("datenday2", "r")
listItems = f.read().splitlines()
array_len = len(listItems)

valid = 0
for x in listItems:
    zahl1 = int(x[0:x.find("-")])
    zahl2 = int(x[x.find("-") + 1:x.find(":") - 1])
    buchstabe = x[x.find(":") - 1:x.find(":")]
    text = x[x.find(":") + 2:len(x)]

    if text[zahl1 - 1:zahl1] != buchstabe and text[zahl2 - 1:zahl2] != buchstabe:
        valid += 0
    elif text[zahl1 - 1:zahl1] == buchstabe and text[zahl2 - 1:zahl2] == buchstabe:
        valid += 0
    else:
        valid += 1
print(valid)

# f = open("datenday2", "r")
# listItems = f.read().splitlines()
# array_len = len(listItems)
#
# valid = 0
# for x in listItems:
#     zahl1 = x[0:x.find("-")]
#     zahl2 = x[x.find("-") + 1:x.find(":") - 1]
#     buchstabe = x[x.find(":") - 1:x.find(":")]
#     text= x[x.find(":") + 2:len(x)]
#     if text.count(buchstabe) >= int(zahl1) and text.count(buchstabe) <= int(zahl2):
#         valid = valid + 1
#         print(x)
#
# print(valid)