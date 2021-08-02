# Converting numbers to words using python program

#Function to convert a single-digit or two-digit number into words
def convertToDigit(n,suffix):
    if n == 0:
        return EMPTY
    if n>19:
        return Y[n//10] + X[n%10] + suffix
    else:
        return X[n] + suffix

# Function to convert a given number into words
def convert(n):
    result = convertToDigit(((n//1000000000)%100), "Billion, ")

    result += convertToDigit(((n//10000000)%100), "Crore, ")

    result += convertToDigit(((n//100000)%100), "Lakh, ")

    result += convertToDigit(((n//1000)%100), "Thousand, ")

    result += convertToDigit(((n//100)%10), "Hundred, ")

    if n > 100 and n%100:
        result += "and "

    result += convertToDigit((n%100), " ")

    return result

if __name__ == "__main__":

    EMPTY = ""
X = [EMPTY, 'one ','two ','three ', 'four ', 'five ', 'six ', 'seven ',
     'eight ', 'nine ', 'ten ','eleven ', 'tweleve ', 'thirteen ', 'fourteen ',
     'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen ']

Y = [EMPTY, EMPTY, "Twenty ", "Thirty ", "Forty ", "Fifty ",
        "Sixty ", "Seventy ", "Eighty ", "Ninety "]

print(convert(888))
