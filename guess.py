import math

print("Think of a number, and I will guess it.")
low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

max_guesses = math.ceil(math.log(high - low + 1, 2))
print(f"I can guess your number in at most {max_guesses} guesses.")

guesses = 0

while low <= high:
    guess = (low + high) // 2
    guesses += 1

    print(f"My guess is: {guess}")
    hint = input("Enter 'l' if too low, 'h' if too high, or 'c' if correct: ").lower()

    if hint == "c":
        print(f"I guessed your number in {guesses} guesses!")
        break
    elif hint == "l":
        low = guess + 1
    elif hint == "h":
        high = guess - 1
    else:
        print("Invalid input. Please enter l, h, or c.")
        guesses -= 1
        continue

    if low > high:
        print("Your hints were inconsistent. Cheating detected.")
        break
