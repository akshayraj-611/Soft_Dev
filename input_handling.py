def get_number_of_properties():
    while True:
        num = input("How many properties do you want to enter? ")
        if num.isdigit():
            num = int(num)
            if num < 0:
                print("Invalid input. Quantity must be positive.")
                continue
            return num
        print("Invalid input, please enter a valid integer.")


def get_property_dimensions(index):
    length = float(input(f"Enter length of property {index}: "))
    width = float(input(f"Enter width of property {index}: "))
    return length, width
