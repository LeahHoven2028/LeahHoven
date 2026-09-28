item = input("What is the item? ")
price = input("What is the price? ")
rate = 1.06875
calculate_tax = (item, price, rate)

price = float(price)
rate = float(rate)

tax = (price * rate)
total = (price + tax)

item = str(item)
tax = float(tax)
total = float(total)

def calculate_tax(item, price, rate):
     return (price * rate)

def calculate_total(item, price, rate):
     tax = calculate_tax(item, price, rate)
     return (price + tax)
print(item + " costs " + str(price) + " dollars before tax and " + str(total) + " after tax")
