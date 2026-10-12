answer = int(input("How fast is the hurricane's wind speed in MPH? \n"))

def hurricane_category():
    if answer < 74:
        print("The hurricane is a tropical storm.")
    elif answer <= 96:
        print("The hurricane is a category 1 hurricane.")
    elif answer <= 111:
        print("The hurricane is a category 2 hurricane.")
    elif answer <= 130:
        print("The hurricane is a category 3 hurricane.")
    elif answer <= 157:
        print("The hurricane is a category 4 hurricane.")
    else:
        print("The hurricane is a category 5 hurricane.")

hurricane_category()
