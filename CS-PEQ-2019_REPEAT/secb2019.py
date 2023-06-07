"""
Write a program that gets two words from the user and then displays a message
saying if the first word can be created using the letters from the second word or not.
"""

def canMake(word1,word2):
    for char in word1:
        if word2.find(char) == -1:
            return False
        else:
            word2 =  word2[:word2.find(char)] + word2[word2.find(char)+1:]
    return True


word1 = input("first word")
word2 = input("second word")
if canMake(word1,word2):
    print("you can make word 1 from word 2")
else:
    print("you cannot make word 1 from word 2")
