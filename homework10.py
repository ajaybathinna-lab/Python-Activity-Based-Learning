total = int(input("Enter total products: "))
defective = int(input("Enter defective products: "))

percentage = defective / total * 100

print("Defect Percentage:", percentage)

if percentage > 5:
    print("Poor Quality")
else:
    print("Good Quality")