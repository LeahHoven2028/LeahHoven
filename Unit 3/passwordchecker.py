attempts = 0

def check_password():
    user_password = input("Please enter your password: ")
    global attempts
    attempts = attempts + 1
    
    
    if user_password == "Wow6767":
        print("Access granted!")
    else:
        print("Access denied!")
        if attempts > 3:
            print("Account locked.")
        else:
            print(str(3 - attempts) + " attempts remaining.")
            check_password()

check_password()
