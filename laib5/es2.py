PIN = 1234

tries = 3

while True:
    insertedPin = int(input("Qual è il pin?\n"))
    if tries > 0:
        if insertedPin == PIN:
            print("Your PIN is correct")
            tries = 3
            exit(0)
        else:
            print("Your PIN is incorrect")
            tries = tries - 1
    else:
        print("Your bank card is blocked")
        exit(0)
