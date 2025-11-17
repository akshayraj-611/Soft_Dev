#A
char = input("Enter a character: ")
max_repeat = int(input("Enter the maximum number of repetitions: "))
repetitions = [char * i for i in range(1, max_repeat + 1)]
print(repetitions)

#B
num = int(input("Enter a number: "))
factors = [int(x) for x in input("Enter factors separated by spaces: ").split()]
products = [num * f for f in factors]
print(products)

#C
numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 != 0]
print("Even numbers among them are:", evens)
print("Odd numbers among them are:", odds)
