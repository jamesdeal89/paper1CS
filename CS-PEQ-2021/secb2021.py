"""
Write a program that asks the user to enter a number, n, and will then calculate and
display the nth Harshad number.
"""

def getHarshadAtIndex(index):
    # continously generate harshad numbers until length is same as index
    harshads = []
    count = 1
    while len(harshads) < index:
        sumOfDigits = 0
        for digit in str(count):
            sumOfDigits += int(digit)
        if count % sumOfDigits == 0:
            harshads.append(count)
        count += 1
    # return the top of the list of harshad numbers
    return harshads[-1]



print(getHarshadAtIndex(int(input("Please enter the index of the harshad number you want:"))))