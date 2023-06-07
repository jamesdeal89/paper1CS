"""
Write a program that asks the user how many numeric digits they would like to enter

and then gets the user to enter that number of numeric digits.
The program should calculate and display the number of times the most frequently
entered numeric digit was input.
"""

def getMode(number):
    data = []
    for _ in range(number):
        data.append(int(input("enter a number:")))
    count = {}
    for number in data:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    numbers = []
    counts = []
    for key in count:
        numbers.append(key)
        counts.append(count[key])
    mode = numbers[counts.index(max(counts))]
    counts.remove(counts.index(max(counts)))
    counts.insert(counts.index(max(counts)),0)
    if mode != numbers[counts.index(max(counts))]:
        print("most common was is " + str(mode))
    else:
        print("Data was multimodal")

print(getMode(int(input("how many numbers to enter:"))))


