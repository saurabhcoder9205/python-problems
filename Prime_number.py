Number = int(input("Enter the Number:"))

is_prime = True
for i in range(2,Number):
    if Number % i == 0:
        is_prime = False
        break

if is_prime and Number>1:
    print("Prime Number")
else:
    print("Not prime Number")
