length = float(input("Please enter the length of the property you want to buy in meters "))
breadth = float(input("Please enter the width of the property you want to buy in meters "))
area = length * breadth
netto = area * 50
tax = netto * 3.5 / 100
brutto = netto + tax
print(f"The total area of the property is {area} m²\nThe net amount to be paid is {netto} €\nTotal taxes adds up to {tax}€ resulting to a total gross amount of {brutto}€ to be paid")