"""
Write a program that asks the user to enter a string. It should then change the order of the vowels in the string and display the result.
"""

def reverseVowels(string):
    vowels = []
    vowelsIndex = [] 
    notVowels = []
    notVowelsIndex = []
    count = 0
    for char in string:
        if char in ["a","e","i","o","u"]:
            vowels.append(char)
            vowelsIndex.append(count)
        else:
            notVowels.append(char)
            notVowelsIndex.append(count)
        count += 1
    vowelsIndex.reverse()
    output = ""
    for i in range(0,len(string)):
        try:
            notVowelsIndex.index(i)
        except ValueError:
            output += vowels[vowelsIndex.index(i)]
        else:
            output += notVowels[notVowelsIndex.index(i)]
    return output


print(reverseVowels(input("Enter string:")))