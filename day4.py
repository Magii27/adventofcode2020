
f = open("datenday4", "r")
listItems = f.read().split("\n\n")
array_len = len(listItems)
print(listItems)

array = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
valid = 0

for x in listItems:
    for x1 in array:
        if x1 == "cid":
            var_prüf = 1
        else:
            if x1 in x:
                prüf = 1
            else:
                prüf = 0
                print(x)
                break
    if prüf == 1:
        valid += 1

print(valid)
