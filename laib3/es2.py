grade = input("enter grade: ")
num = 0.0

grade = grade.upper()
grade = grade.replace("F", "E")

if (len(grade) < 3 and grade[0] >= "A" and grade[0] <= "F"):
    num = 4 - (ord(grade[0]) - ord("A"))
    if (num < 4 and num > 0 and len(grade) > 1):
        if (grade[1] == "+"):
            num = num + 0.3
        if (grade[1] == "-"):
            num = num - 0.3
    print("il voto è", num)
else:
    print("error")
