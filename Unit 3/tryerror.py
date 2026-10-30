def mult():
    num_one = input("Give a number. \n")
    num_two = input("Give another number. \n")
    try:
        print(float(num_one) * float(num_two))
    except:
        print("Invalid input. Try again. \n")
        mult()

mult()
