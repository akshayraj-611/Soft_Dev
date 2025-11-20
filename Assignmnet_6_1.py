def area(length,width) :
    return length * width

def gross_price (area) :
    return area * 1.1

properties = []
while True:
    num_properties = input("How many properties do you want to enter? ")
    if num_properties.isdigit():
        num_properties = int(num_properties)
        if num_properties < 0:
            print("Invalid input..quantity needs to be positive")
            continue
        break
    else:
        print("Invalid input, please enter an integer number")
        

for i in range(num_properties):
    length = float(input(f"Enter length of property {i+1}: "))
    width = float(input(f"Enter width of property {i+1}: "))
    properties.append((length, width))

for idx, (length, width) in enumerate(properties):
    net = area(length, width)
    gross = gross_price(net)
    print(f"Property {idx+1}: Net Price = {net}€, Gross Price = {gross}€")

