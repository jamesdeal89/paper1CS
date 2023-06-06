# RLE

def RLE(string):
    output = ""
    count = 1
    for position in range(len(string)):
        if position < len(string)-1:
            if string[position] == string[position + 1]:
                count += 1
            else:
                output += string[position] + " " + str(count) + " "
                count = 1
        else:
            output += string[position] + " " + str(count) + " "
    return output

print(RLE(input("Enter string to be compressed:")))
