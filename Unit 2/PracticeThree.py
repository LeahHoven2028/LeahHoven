band = input("What is your favorite band? ")
num_people = input("How many people are going to the concert? ")
ticket_price = input("What is the price of a ticket? ")

def show_cost(band, num_people, ticket_price):
    total_cost = int(num_people) * float(ticket_price)
    print("The total cost for " + num_people + " people to see " + band + " is $" + str(total_cost) + ".")

show_cost(band, num_people, ticket_price)