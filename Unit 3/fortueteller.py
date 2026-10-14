print("Welcome to the fortune teller! \n")
import random
def fortune_teller():
    try:
        input_one = int(input("What is your lucky number? \n"))
        input_two = int(input("What age do you want to live to? \n"))
        input_three = float(input("How far into the furture do you wanna see? \n"))
        awnser = (input_two + (random.randrange(1,10)))
        threetwo = (input_three + input_two)

        if threetwo < 10:
            print("Tomorrow is your last day.")
        elif 10 < threetwo < 50:
            print("You will live to the age of " + awnser + ".")
        elif 50 < threetwo < 100:
            print("You will live forever.")
        else:
            print("You will live for " + awnser + "years.")
    except:
        print("Invalid input. Try again. \n")

fortune_teller()
