def is_sentence_palindrome(sentence):
    cleaned_sentence = "".join(char.lower() for char in sentence if char.isalnum())
    if cleaned_sentence == cleaned_sentence[::-1]:
        return True
    else:
        return False
    
my_sentence = input ("Enter a sentence to check whether it's a Palindrome ")
if is_sentence_palindrome(my_sentence) == True :
    print(f"Yes, the sentence:' {my_sentence}' is a Palindrome")
else :
    print(f"No, the sentence: '{my_sentence}' is not a Palindrome ")
