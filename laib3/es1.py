num = []

for i in range(3):
    num.append(int(input(f"Scrivi il numero {i + 1}\n")))

if (num[2] > num[1] and num[1] > num[0]):
    print("increasing")
elif (num[2] < num[1] and num[1] < num[0]):
    print("decreasing")
else:
    print("neither")
