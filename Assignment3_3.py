text = input("Enter a text to count the frequency of the words appearing in it: ")
text = text.lower()
words = text.split()
counted_words = []

print(" Word frequencies:")

for word in words:
    if word not in counted_words:
        frequency = words.count(word)
        print(f"{word}: {frequency}")
        counted_words.append(word)
