numbers = []
while True:
    user_input = input("Enter an integer (or type 'stop' to finish): ")
    if user_input.lower() == "stop":
        break
    elif user_input.isdigit():
        number= int(user_input)
        numbers.append(number)
    else:
        print("Please enter a valid integer.")

if len(numbers) > 0:
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0

    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
        total += num
    mean = total / len(numbers)
    print(f'The Minimum is ----> {minimum} ')
    print(f'The Maximum is ----> {maximum} ')
    print(f'The Mean is    ----> {mean} ')
else :
    print("You haven't entered any Integers")
