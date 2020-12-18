def main():
    fileParolacce = open("es5input2.txt", "r")
    fileDaCorreggere = open("es5input1.txt", "r")
    text = fileDaCorreggere.read()
    fileDaCorreggere.close()
    fileDaCorreggere = open("es5input1.txt", "w")

    line = fileParolacce.readline()
    setParolacce = {line.strip()}
    while line != "":
        setParolacce.add(line.strip())
        line = fileParolacce.readline()

    isWord = False
    textNew = ""
    word = ""
    text = " " + text + " "
    for chr in text:
        if not isWord and (chr.isalpha() or chr in "-+*_"):
            word += chr
            isWord = True
        elif isWord and (chr.isalpha() or chr in "-+*_"):
            word += chr
        elif isWord and not (chr.isalpha() or chr in "-+*_"):
            if word.lower() in setParolacce:
                word = len(word) * "*"
            textNew += word
        if not (chr.isalpha() or chr in "-+*_"):
            word = ""
            textNew += chr
            isWord = False

    textNew = textNew.strip()
    fileDaCorreggere.write(textNew)
    fileParolacce.close()
    fileDaCorreggere.close()


main()
