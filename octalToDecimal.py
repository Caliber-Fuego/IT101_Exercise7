oString = input("Enter a string of octal digits: ")
octal = 0
exponent = len(oString) - 1 #takes the number of digits or length in oString and subtracts it by 1
for x in oString: #loops through the items in oString and performs the algorithm on each item
    octal += int(x) * 8 ** exponent
    exponent = exponent - 1
print("The integer value is:", octal)