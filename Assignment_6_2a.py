def is_palindrome(string):
    string = string.lower()
    check_pal = string[::-1]
    if check_pal == string:
        return True
    else:
        return False

my_string = input("Enter a string to check whether its a Palindrome ")
if is_palindrome(my_string) == True:
    print(f"Yes, {my_string} is a Palindrome")
else :
    print(f"No, {my_string} is not a Palindrome")