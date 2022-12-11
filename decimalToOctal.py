decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
    print(0)
else:
    print("Quotient, Remainder, Octal")
    oString = ""
    while decimal > 0: #loops until decimal is not greater than 0
        remainder = decimal % 8
        decimal = decimal // 8
        oString = str(remainder) + oString
        print("%5d%8d%12s" % (decimal, remainder, oString))
                #%5d prints an integer that uses 5 spaces
                #%8d does the same as above but uses 8 spaces
                #%12s prints a string and uses 12 spaces
    print("The Binary representation is", oString)