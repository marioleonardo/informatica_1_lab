def main():
    string1 = "es6input.txt"
    string1 = string1.replace(" ", "")
    string2 = "es6output.txt"
    string2 = string2.replace(" ", "")
    key = input("chiave: \n")
    modalita = input("encode or decode? (e/d)\n")
    modalita = 1 if modalita == "d" else 0
    key = keyTransform(key)
    tupla = fromKeyToCifrario(key)
    cifrario = tupla[0]
    alphabet = tupla[1]

    try:
        file1 = open(string1, 'r')
        file2 = open(string2, 'w')
    except:
        print("file not correct")
        return

    textEncrypted = ""
    twoCharacters = []
    character = file1.read(1)
    while character != "":
        character = character.lower()
        if character in alphabet and modalita == 0:
            if len(twoCharacters) < 1:
                twoCharacters.append(character)
            else:
                twoCharacters.append(character)
                textEncrypted += "".join(encryptTwoCharacters(twoCharacters, cifrario))
                twoCharacters = []
        elif character in cifrario and modalita == 1:
            if len(twoCharacters) < 1:
                twoCharacters.append(character)
            else:
                twoCharacters.append(character)
                textEncrypted += "".join(encryptTwoCharacters(twoCharacters, cifrario))
                twoCharacters = []
        else:
            textEncrypted += character
        character = file1.read(1)
    if len(twoCharacters) > 0:
        textEncrypted += twoCharacters[0]
    file2.write(textEncrypted)
    file1.close()
    file2.close()


def encryptTwoCharacters(twoCharacters, cifrario):
    twoCharactersResult = []
    matrix = []
    listaTemp = []
    for i in range(len(cifrario)):
        listaTemp.append(cifrario[i])
        if (i + 1) % 5 == 0:
            matrix.append(listaTemp)
            listaTemp = []

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == twoCharacters[0] or (twoCharacters[0] in "ij" and matrix[r][c] in "ij"):
                character1r = r
                character1c = c
            if matrix[r][c] == twoCharacters[1] or (twoCharacters[1] in "ij" and matrix[r][c] in "ij"):
                character2r = r
                character2c = c
    if character1c == character2c:
        twoCharactersResult.append(matrix[character2r][character2c])
        twoCharactersResult.append(matrix[character1r][character1c])
    else:
        twoCharactersResult.append(matrix[character1r][character2c])
        twoCharactersResult.append(matrix[character2r][character1c])
    return twoCharactersResult


def fromKeyToCifrario(key):
    alphabet = ""
    cifrario = key
    for i in range(26):
        alphabet += chr(ord("a") + (i))
    for element in alphabet:
        if element not in cifrario and (
                ("i" not in cifrario and "j" not in cifrario) or (element != "i" and element != "j")):
            cifrario += element
    return cifrario, alphabet


def keyTransform(key):
    key = key.strip()
    key = key.lower()
    keyTemp = ""
    for i in key:
        if i.isalpha() and i not in keyTemp and \
                (("i" not in keyTemp and "j" not in keyTemp) or (i != "i" and i != "j")):
            keyTemp = keyTemp + i
    key = keyTemp
    return key


main()
