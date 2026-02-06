import random

print("=== Guess The Number ===")

number = random.randint(1, 10)

while True:
    guess = int(input("Guess (1–10) or 0 to reveal: "))

    if guess == 0:
        print("Alright, tapping out huh 😭")
        print("The correct number was:", number)
        break

    if guess == number:
        print("Wayy! You nailed it 🎯")
        break
    else:
        print("Nope, try again!")
