letters = ['H', 'P', 'E', 'E', 'L', 'T', 'L', 'E', 'O', 'R']

hello = [ch for i, ch in enumerate(letters) if i % 2 == 0]
peter = [ch for i, ch in enumerate(letters) if i % 2 == 1]

print(hello) 
print(peter)  
