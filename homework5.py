id = int(input("Enter transaction ID: "))
amount = int(input("Enter amount: "))

transaction = (id, amount)

print("Transaction:", transaction)

if amount > 0:
    print("Valid Transaction")
else:
    print("Invalid Transaction")