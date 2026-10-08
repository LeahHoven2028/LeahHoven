question_one = input("What is 9*9? \n")
question_two = input("What is 3^3? \n")
question_three = input("How much is VIP on Flee The Facility? \n")
question_four = input("How much did Bloxburg cost? \n")
question_five = input("How many players are able to be in Flee the Facility? \n")


def tally_score():
    if question_one == "81":
        print("Correct!")
    else:
        print("Incorrect.")
    if question_two == "27":
        print("Correct!")
    else:
        print("Incorrect.")
    if question_three == "420":
        print("Correct!")
    else:
        print("Incorrect.")
    if question_four == "25":
        print("Correct!")
    else:
        print("Incorrect.")
    if question_five == "6":
        print("Correct!")
    else:
        print("Incorrect.")

print(tally_score())
