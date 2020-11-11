def countVowels(string):
    count = 0
    for char in string:
        if char in "aeiouAEIOU":
            count = count + 1
    return count


print(countVowels(input("Parola?")))
