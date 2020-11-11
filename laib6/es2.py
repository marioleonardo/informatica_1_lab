def countWords(string):
    if string[len(string) - 1].isspace():
        count = 0
    else:
        count = 1
    oldChar = " "
    for char in string:
        if char.isspace() and (not oldChar.isspace()):
            count = count + 1

        oldChar = char
    return count


print(countWords(input("Frase?\n")))
