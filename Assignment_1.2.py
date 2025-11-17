dog_age = int(input("How old is your Dog? "))
if dog_age == 1:
    print ("Your Dog's age corresponds to 14 human years")
elif dog_age == 2:
    print ("Your Dog's age corresponds to 22 human years")
elif dog_age == 0:
    print(" Sorry...!! Insufficient Information")
else :
    print (f"Your Dog's age corresponds to {(dog_age -2)*5 +22} human years ")