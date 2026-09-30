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
