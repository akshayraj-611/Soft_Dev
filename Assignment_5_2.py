import random
while True :
    while True:
        lower_limit = input("Define the lower limit of your interval: ")
        if not lower_limit.isdigit():
            print("Please provide a Valid Integer input.")
            continue
        lower_limit = int(lower_limit)
        break
    while True:
        upper_limit = input("Define the upper limit of your interval: ")
        if not upper_limit.isdigit():
            print("Please provide a Valid Integer input.")
            continue
        upper_limit = int(upper_limit)
        break
    if upper_limit > lower_limit:
        break
    else :
        print("Invalid intervals..please redo ")

secret_number = random.randint(lower_limit, upper_limit + 1)
counter = 1
while counter <= 5:
    while True:
        your_number = int(input("Guess the Secret Number: "))
        if your_number > lower_limit and your_number < upper_limit:
            break
        else:
            print("Choose a number between the given Intervals please..!")
    if your_number == secret_number:
        print(f"Hurrayy!!{your_number} was the secret number. You guessed it right. You win.")
        break
    else: 
        print(f"Oops, close enough, but not right there. you have {5-counter} attempts left.")
        if your_number > secret_number:
            print("Your number is higher than the secret number")
        else:
            print("Your number is lower than the secret number")
    counter += 1

if counter == 6:
    print("Sorry, you lose.. Better Luck next time...!!")
    print(f"The Secret number was : {secret_number}")
