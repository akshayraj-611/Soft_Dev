from calculations import area, gross_price
from input_handling import get_number_of_properties, get_property_dimensions
from display import show_property_prices

def main():
    properties = []
    num_properties = get_number_of_properties()

    for i in range(1, num_properties + 1):
        length, width = get_property_dimensions(i)
        properties.append((length, width))

    for idx, (length, width) in enumerate(properties, start=1):
        net = area(length, width)
        gross = gross_price(net)
        show_property_prices(idx, net, gross)

if __name__ == "__main__":
    main()
