import random
random.randint(1,100)
Jackpot = random.randint(1,100)
Guess = int(input("Enter the number:"))
counter = 1
Max_attemps = 5
while Guess!= Jackpot and counter<Max_attemps:
    if Guess<Jackpot:
        print("Guess higher")
    else:
        print("Guess lower")
    Guess = int(input("Enter the number:"))
    counter += 1

if Guess == Jackpot:
    print("Right Guess!")
    print("You took",counter,"attemps")
else:
    print("Game over! You've used all",Max_attemps,"attemps")
    print("The correct number",Jackpot)
    
