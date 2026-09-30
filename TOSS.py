user_choice_0 = input("Enter your choice E - even and O - odd").upper()
user_in_1 = int(input("Enter any number between 1 to 6"))
while True:
    try:
        if 1 <= user_in_1 <= 6:
            break
        else:
            print("Enter a valid number")
    except ValueError:
      print("Invalid Input , Pls Do acc to instructions")

comp_out_1 = random.randint(1, 6)
if (user_in_1 + comp_out_1) % 2 == 0:
    if user_choice_0 == "E" or user_choice_0 == "e":
        bat_bowl = input("Enter your choice for A-Batting first and B-Bowling first")
        if bat_bowl == "A" or bat_bowl == "a":
            bat_first()
        else:
            bowl_first()
    else:
        x = random.randint(1, 2)
        if x == 1:
            bat_first()
        else:
            bowl_first()
elif (user_in_1 + comp_out_1) % 2 != 0:
    if user_choice_0 == "O" or user_choice_0 == "o":
        bat_bowl = input("Enter your choice for A-Batting first and B-Bowling first").upper()
        if bat_bowl == "A":
            bat_first()
        else:
            bowl_first()
    else:
        x = random.randint(1, 2)
        if x == 1:
            bat_first()
        else:
            bowl_first()
else:
    print("Please follow the instructions properly")
