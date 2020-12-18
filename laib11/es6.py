def main():
    file = open("es6input.txt", "r")
    dictNations = {}
    line = file.readline().lower()
    while line != "":
        listaTemp = line.split()
        dictNations.update({" ".join(listaTemp[1:-1]): listaTemp[-1]})
        line = file.readline().lower()
    file.close()

    nation = input("nazione? \n").lower().strip()
    while nation != "-1":
        a = dictNations.get(nation, "-1")
        if a != "-1":
            print(a)
            print()
        nation = input("nazione? \n").lower().strip()


main()
