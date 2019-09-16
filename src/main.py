# Author: Jahnoah Simpson
# Version: 1.0

# Converts the letters in a number base 11 or higher into decimal values
# [A = 10], [B = 11], [...], [Z = 35]
def affixNumbers(value):
    uniValue = ord(str(value).upper())
    if(uniValue >= 48 and uniValue <= 57):
        return int(value)
    elif(uniValue >=  65 and uniValue <= 90):
        return int(uniValue - ord('A') + 10)
    else:
        print("Invalid input detected... Please try again.")

# Converts all digits with values greater than nine into letters
# [10 = A], [11 = B], [...], [35 = Z]
def affixLetters(value):
    if(value <= 9):
        return str(value)
    elif(value > 9):
        return chr(value + ord('A') - 10)

def toDecimal(num, numBase):
    decimalNum = 0
    reverseDigits = list(num)[::-1]

    for placeValue, digit in enumerate(reverseDigits):
        decimalNum += eval(digit) * eval(numBase) ** placeValue

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