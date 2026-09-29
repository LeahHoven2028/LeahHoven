num_apples = float(input("How many apples do you have? "))
num_people = int(input("How many people are there? "))

def serve(num_apples, num_people):
    print("Serve " + (num_people) + "glasses of apple juice to " + (num_apples) + " per glass.")

def portion(num_apples, num_people):
    calculate = float(num_apples) / int(num_people)
    return calculate

def divide(num_apples, num_people):
    calculate = float(num_apples) / int(num_people)
    return calculate

calculate = divide(num_apples, num_people)

print("Each person will get " + str(calculate) + " apples per glass of apple juice.")
