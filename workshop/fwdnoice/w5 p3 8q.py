import random
number = random.randint(1, 20)
num_guesses = 5
for i in range(num_guesses):
    guess = int(input("Guess a number between 1 and 20: "))
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Congratulations! You guessed the number.")
        break
else:
    print("Sorry, you ran out of guesses.")
    print("The number was:", number)
