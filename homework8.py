book = int(input("Enter book ID: "))
days = int(input("Enter delayed days: "))

if days > 0:
    fine = days * 2
    print("Book ID:", book)
    print("Fine:", fine)
else:
    print("No Fine")