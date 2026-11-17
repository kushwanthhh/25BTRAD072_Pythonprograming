import random

while True:

    print("\n===== DICE SIMULATOR =====")

    n = int(input("Enter number of dice to roll: "))

    if n <= 0:
        print("Please enter a valid number!")
        continue

    print("\nRolling the dice...")

    for i in range(n):
        result = random.randint(1, 6)
        print("Dice", i + 1, ":", result)

    choice = input("\nRoll again? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you for playing!")
        break
