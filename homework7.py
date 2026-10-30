price = 50
stock = 20

quantity = int(input("Enter quantity: "))

if quantity <= stock and quantity > 0:

    bill = quantity * price
    stock = stock - quantity

    print("Total Bill:", bill)
    print("Remaining Stock:", stock)

else:
    print("Stock Not Available")