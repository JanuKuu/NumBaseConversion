# Author: Jahnoah Simpson
# Version: 1.0

def toDecimal(num, numBase):
    decimalNum = 0
    placeValue = 0
    reverseDigits = list(num)[::-1]

    for digit in reverseDigits:
        decimalNum += eval(digit) * eval(numBase) ** placeValue
        placeValue += 1

    return decimalNum

def main():
    num = input("Enter the number you wish to convert: ")
    base = input("Enter the base of your number: ")

    print("Your number [", num, "] in decimal is: ", toDecimal(num, base))

    if(input("\nConvert another number? ('y' or 'n'): ") == 'y'):
        main()
    else:
        print("Stopping program now. Thank you!")

print("Starting non-decimal number to decimal converter...\n")
main()