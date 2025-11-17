number = int(input("Enter the number of characters you want at the longest point in your triangle. "))
counter = 1
while counter <=  number :
    print ('#'*counter)
    counter +=1
counter = number -1
while counter > 0:
    print('#' * counter)
    counter -= 1
