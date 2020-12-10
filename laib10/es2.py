def main():
    file1 = open('./es2input.txt', 'r')
    file2 = open('./es2output.txt', 'w')
    text = file1.read()
    text = text.split("\n")
    text = text[::-1]
    text = "\n".join(text)
    file2.write(text)
    file1.close()
    file2.close()


main()
