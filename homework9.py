passengers = int(input("Enter passengers: "))
capacity = int(input("Enter bus capacity: "))

buses = (passengers + capacity - 1) // capacity

print("Required Buses:", buses)