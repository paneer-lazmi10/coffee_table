#Choose integers 1 to 6
#Round 1 is for choosing batting or bowling 1 over each
#Round 2 is for playing your chance
#Winner will be declared in the last
import random
import array


def bat():
    t = array.array('i', [])
    for i in range(1, 7):
        while True:
            try:
               u = int(input(f"Enter a number between 1 and 6 for batting ;Ball = {i} "))
               if 1 <= u <= 6:
                break
               else:
                    print("Enter a valid number")
            except ValueError:
                print("Invalid Input , Pls Do acc to instructions")


        c = random.randint(1, 6)
        print(f"Computer chose: {c}")
        if u != c:
            t.append(u)
        else:
            print("Player Out")
            break
    print(t)
    return t


def bowl():
    t = array.array('i', [])
    for i in range(1, 7):
        while True:
            try:
                u = int(input(f"Enter a number between 1 and 6 for bowling ;Ball = {i} "))
                if 1 <= u <= 6:
                    break
                else:
                    print("Enter a valid number")
            except ValueError:
                print("Invalid Input , Pls Do acc to instructions")



        c = random.randint(1, 6)
        if u != c:
            t.append(c)
        else:
            print("Player Out")
            break
    print(t)
    return t


def bat_first():
    A = bat()
    t1 = sum(A)
    print(t1)
    print("Now bowl!")
    B = bowl()
    t2 = sum(B)
    print(t2)
    if t1 == t2:
        print(f"Its a draw T1 = {t1} and T2 = {t2}")
    elif t1 > t2:
        print(f"its a win for you!! T1 = {t1} and T2 = {t2}")
    else:
        print(f"its a win for the computer!! T1 = {t1} and T2 = {t2}")


def bowl_first():
    C = bowl()
    t1 = sum(C)
    print("Now bat!")
    D = bat()
    t2 = sum(D)
    if t1 == t2:
        print("Its a draw")
    elif t1 > t2:
        print("its a win for you!!")
    else:
        print("its a win for the computer!!")


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















