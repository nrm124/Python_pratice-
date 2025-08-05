print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("you can rude")
    age = int(input("what is your age "))
    if age <=12:
        bill = 5
    elif age <=18:
        bill = 7
    else:
        bill = 12

    wants_photo = input("do you want to have a photo take? type Y for yes and N for No")
    if wants_photo == "y":
        bill += 3
    print(f"your total ticket is {bill}")
else:
    print(f"you can't ride")