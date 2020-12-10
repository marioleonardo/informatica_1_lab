def main():
    string1 = "es5input.txt"
    string1 = string1.replace(" ", "")
    string2 = "es5output.txt"
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
    character = file1.read(1)
    while character != "":
        character = character.lower()
        if character in alphabet and modalita == 0:
            characterEncrypted = cifrario[alphabet.index(character)]
            textEncrypted += characterEncrypted
        elif character in cifrario and modalita == 1:
            characterEncrypted = alphabet[cifrario.index(character)]
            textEncrypted += characterEncrypted
        else:
            textEncrypted += character
        character = file1.read(1)
    file2.write(textEncrypted)
    file1.close()
    file2.close()


def fromKeyToCifrario(key):
    alphabetReversed = ""
    alphabet = ""
    cifrario = key
    for i in range(26):
        alphabetReversed += chr(ord("a") + (25 - i))
        alphabet += chr(ord("a") + (i))
    for element in alphabetReversed:
        if element not in key:
            cifrario += element
    return cifrario, alphabet


def keyTransform(key):
    key = key.strip()
    key = key.lower()
    keyTemp = ""
    for i in key:
        if i.isalpha() and i not in keyTemp:
            keyTemp = keyTemp + i
    key = keyTemp
    return key


main()
