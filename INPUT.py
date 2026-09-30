def get_user_input(prompt):
    while True:
        try:
            u = int(input(prompt))
            if 1 <= u <= 6:
                return u
            else:
                print("Enter a valid number between 1 and 6")
        except ValueError:
            print("Invalid Input, please follow instructions")
