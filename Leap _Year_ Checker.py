Year = int(input("Enter the Year do you wnat check:"))

if (Year % 4 == 0 and Year % 100 != 0 )or  (Year % 400 == 0):
    print("This is leap year")
else:
    print("Not leap year")
