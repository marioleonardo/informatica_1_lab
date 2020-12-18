import random as rd


def main():
    arraySparsoA = [rd.randint(1, 10) * rd.randint(0, 1) * rd.randint(0, 1) for index in range(20)]

    arraySparsoB = [rd.randint(1, 10) * rd.randint(0, 1) * rd.randint(0, 1) for index in range(20)]
    print(sparseArraySum(arraySparsoA, arraySparsoB))


def sparseArraySum(arrayA, arrayB):
    dictA = convertArrayToDict(arrayA)
    dictB = convertArrayToDict(arrayB)
    dictNew = {}
    setKeys = set(dictA.keys())
    setKeys.update(set(dictB.keys()))
    for key in setKeys:
        dictNew.update({key: sum([dictA.get(key, 0), dictB.get(key, 0)])})
    arrayNew = convertDictToArray(dictNew)
    return arrayNew


def convertArrayToDict(array):
    dict = {}
    for index in range(len(array)):
        if array[index] != 0:
            dict.update({index: array[index]})

    return dict


def convertDictToArray(dict):
    array = []
    for index in range(max(dict.keys()) + 1):
        if index in dict:
            array.append(dict[index])
        else:
            array.append(0)

    return array


main()
