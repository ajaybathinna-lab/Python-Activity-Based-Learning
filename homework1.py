capacity = int(input("Enter capacity: "))
passengers = int(input("Enter passengers: "))

boarding = int(input("Enter boarding: "))
leaving = int(input("Enter leaving: "))

passengers = passengers + boarding - leaving

print("Total passengers:", passengers)

if passengers > capacity:
    print("Capacity exceeded")
else:
    print("Capacity normal")