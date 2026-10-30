prepared = int(input("Enter prepared meals: "))
served = int(input("Enter served meals: "))

leftover = prepared - served

percentage = leftover / prepared * 100

print("Leftover:", leftover)
print("Wastage:", percentage)

if percentage > 10:
    print("High Wastage")
else:
    print("Low Wastage")