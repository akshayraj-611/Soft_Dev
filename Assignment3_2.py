#A
customers = [
    ["Max", "Mustermann", "01.01.83"],
    ["Martina", "Musterfrau", "02.02.84"],
    ["Gabi", "Meier", "03.03.85"]
]

last_names = []
for person in customers:
    last_names.append(person[1])
print(last_names)

#B
numbers = [1, 4, 2, 8, 5]
squared_numbers = []

i = 0
while i < len(numbers):
    squared_numbers.append(numbers[i] **2)
    i += 1
print(squared_numbers)

#C
import random
secret_number = random.randint(1,100)
for i in range(10**2):
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > secret_number:
        print("Too high! Guess again.")
    elif guess < secret_number:
        print("Too low! Guess again.")
    else:
        print("You guessed it! The number was", secret_number)
        break
