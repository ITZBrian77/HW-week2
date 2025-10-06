from random import randint

random_number = randint(0, 25)
guess_number = int(input("Guess a number between 0 and 25: "))

if random_number == guess_number:
    print("You Win!")
else:
    print("You Lose! GG. The correct number was", random_number)
