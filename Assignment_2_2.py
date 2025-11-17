k = int(input ("Enter the number of strings you want to input. "))
strings = []
for i in range(k):
    word = input(f"Enter the string {i + 1}: ")
    strings.append(word)
total_length = 0
for word in strings:
    total_length += len(word)
print("The total length of all words entered combined is:", total_length)