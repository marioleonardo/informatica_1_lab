def main():
    file1 = open('./es1input.txt', 'r')
    file2 = open('./es1output.txt', 'w')
    text = ""
    index = 1
    for riga in file1:
        text = text + "/*" + str(index) + "*/" + riga
        index += 1

    file2.write(text)
    file1.close()
    file2.close()


main()
