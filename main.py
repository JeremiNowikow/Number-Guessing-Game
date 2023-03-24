from random import randint

# Function that prompts the user to enter a number and then returns it as an integer
def guessNumber() -> int:
    while True:
        n = input("Guess the number in range of 1 to 100: ")
        try:
            return int(n)
        except ValueError:
            print("It's not a number!")


number_to_guess = randint(1, 100) # The number the user is supposed to guess

while True:
    user_number = guessNumber()
    if user_number < number_to_guess:
        print("Too small!")
    elif user_number > number_to_guess:
        print("Too big!")
    else:
        print("You win!")
        break

