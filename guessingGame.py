import random
print("Number Guessing Game")
randomNumber = random.randint(1, 9)
chances = 0
while chances < 5:
    guess = int(input("Enter Your Guess: "))
    if guess == randomNumber:
        print("Congo! You won!")
        break
    elif guess < randomNumber:
        print("Your Guess Was Too Low! Guess A Higher Number", guess)

    else:
        print("Your Guess Was Too High! Guess A Lower Number", guess)

    chances += 1
if not chances < 5:
    print("Sed! You Lost! The Number is: ", randomNumber)
