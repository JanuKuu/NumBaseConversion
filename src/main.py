# Author: Jahnoah Simpson
# A program to convert the base of any number
# Version: 2.0 (non-decimal conversion support)

# Converts the letters in a number base 11 or higher into decimal values
# [A = 10], [B = 11], [...], [Z = 35]
def affixNumbers(value):
    uniValue = ord(value.upper())
    if(uniValue >= 48 and uniValue <= 57):
        return int(value)
    elif(uniValue >=  65 and uniValue <= 90):
        return int(uniValue - ord('A') + 10)

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
        decimalNum += affixNumbers(digit) * int(numBase) ** placeValue

    return decimalNum

def toNewBase(num, base, newBase):
    newNum = ""
    remainder = toDecimal(num, base)

    while(remainder > 0):
        remainder, newDigit = divmod(remainder, int(newBase))
        newNum = affixLetters(newDigit) + newNum
    
    return newNum

def checkErrors(num, base, newBase):
    if(num.isalnum() and base.isnumeric() and newBase.isnumeric()):
        if(int(newBase) < 37):
            for digit in num:
                if(int(base) - affixNumbers(digit) < 1):
                    print("\nDigit values can not be higher than base. Please try again...")
                    return False
            return True
        else:
            print("\nCan not convert to numbers above base 36. Please try again...")
            return False
    else:
        print("\nInvalid input detected. Please try again...")
        return False

def main():
    num = input("Enter the number you wish to convert: ")
    base = input("Enter the base of your number: ")
    newBase = input("Enter the base you wish to convert to: ")
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉") # Didn't know subscript was a thing. Thanks Stackoverflow! 

    if(checkErrors(num, base, newBase)):
        print("Your number [" + num.upper() + base.translate(SUB) + "] in base", newBase, "is:", toNewBase(num, base, newBase))

        if(input("\nConvert another number? (y or n): ") == 'y'):
            main()
        else:
            print("Stopping program now. Thank you!")
            exit()
    else:
        main()

print("Starting number base converter...\n")
main()