import random
random.randint(1,100)
Jackpot = random.randint(1,100)
Guess = int(input("Enter the number:"))
counter = 1
while Guess!= Jackpot:
    if Guess<Jackpot:
        print("Guess higher")
    else:
        print("Guess lower")
    Guess = int(input("Enter the number:"))
    counter += 1
print("Right Guess")
print("You took",counter,"attemps")
