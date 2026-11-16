import random
number = random.randint(1, 100) while True:
guess = int(input("Enter your guess (1-100): ")) if guess == number:
print("Congratulations! You guessed the correct number.") break
elif guess < number: print("Too low! Try again.")
else:
print("Too high! Try again.")OUPTUT: Name = input(“Enter your name : “) Print(name)
num = int(input("Enter a number: ")) factorial = 1
for i in range(1, num + 1): factorial = factorial * i
print("Factorial =", factorial)
