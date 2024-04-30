name = input("Howdy Pal! What's your name?: ")
int1 = int(input(f"Heyyy there {name}, would you be so kind as to chose an integer between 1 and 100?: "))
if 100 >= int1 >= 1:
    if int1 % 2 == 0:
        if 24 >= int1 >= 2:
            print("Even and less than 25")
        if 60 >= int1 >= 26:
            print("Even and between 26 and 60 inclusive")
        if 100 >= int1 > 60:
            print("Even and greater than 60")
    elif int1 % 2 != 0 and int1 < 60:
        print("Odd and less than 60")
    elif int1 % 2 != 0 and int1 > 60:
        print("Odd and greater than 60")
else:
    print("not a valid number")

print(f"Thanks for playing my game {name}. Have a nice life.")