a = int(input("Enter Team A score: "))
b = int(input("Enter Team B score: "))

if a > b:
    print("Team A is Winner")
elif b > a:
    print("Team B is Winner")
else:
    print("Both are Equal")