class String(str):
    def reversed(self):
        stringaNew = self[::-1]
        return stringaNew


stringa = input("Qual é la stringa?\n")
stringa = String(stringa)
print(stringa.reversed())
