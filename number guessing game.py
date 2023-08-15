import random

num = input("Enter the range of the numbers: ")

if num.isdigit():
    num = int(num)
elif num <= 0:
    print("Enter a number greater than zero!")
    quit()
else:
    print("Enter a valid number!")
    quit()

random_number = random.randrange(num)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a valid number!")
        continue

    if user_guess == random_number:
        print("Great Guess! You got it!")
        break
    elif user_guess > random_number:
        print("Try again :(")
        print("You were above the number!")
    else:
        print("Try again :(")
        print("You were below the number!")
    
print(f"You got it in {guesses} guesses!")


