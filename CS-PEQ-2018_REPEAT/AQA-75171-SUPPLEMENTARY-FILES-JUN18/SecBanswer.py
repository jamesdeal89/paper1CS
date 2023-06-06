# Write a program that checks which numbers from a series of numbers entered by the user are prime. 
# PASSES TEST

def isPrime(number):
    for test in range(2,number):
        if number % test == 0:
            return False
    return True

repeat = True
while repeat:
    number = int(input("Enter a number:"))
    if number <= 1:
        print("not greater than 1")
    elif isPrime(number):
        print("is prime")
    else:
        print("is not prime")
    cont = input("type y to stop or enter to enter another:").strip().lower()
    if cont == "y":
        repeat = False
