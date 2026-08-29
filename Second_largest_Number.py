def second_greatest_manual(a, b, c):
    if (a >= b and a <= c) or (a <= b and a >= c):
        return a
    elif (b >= a and b <= c) or (b <= a and b >= c):
        return b
    else:
        return c


print(f"Second Greatest: {second_greatest_manual(10, 45, 25)}")
