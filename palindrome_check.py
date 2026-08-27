Num = int(input("Enter the number:"))

temp = Num
reversed_num = 0
while temp >0:
    remainder = temp % 10
    reversed_num = (reversed_num * 10) + remainder
    temp = temp // 10

if Num == reversed_num:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")
    