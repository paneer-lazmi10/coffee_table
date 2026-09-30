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
