def main():
    file = open("es7input.txt", "r")
    dictPositions = {}
    text = file.read().lower()
    listaCelle = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    r = 0
    c = 0
    index = 0
    while index < len(text):
        if text[index] == " ":
            position = (int(r), int(c))
            dictPositions.update({position: ""})
        c += 1
        if text[index] == "\n":
            r += 1
            c = 0
        index += 1
    file.close()

    for key in dictPositions:
        rkey, ckey = key
        listaCorridoiVicini = []
        for index in range(4):
            if (rkey + listaCelle[index][0], ckey + listaCelle[index][1]) in dictPositions:
                listaCorridoiVicini.append((rkey + listaCelle[index][0], ckey + listaCelle[index][1]))
        dictPositions[key] = set(listaCorridoiVicini)
    print(dictPositions)


main()
