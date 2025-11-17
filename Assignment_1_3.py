print("Greetings!!!")
year = int(input("Enter the year you want to check for leap year. "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a Leap Year")
        else:
            print(f"The year {year} is NOT a Leap Year")
    else :
        print(f"The year {year} is a Leap Year")
else :
    print(f"The year {year} is NOT a Leap Year")