def make_pizza(*toppings):
    """print all the toppings"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def sand_wiches(*toppings):
    print("This sand_wiches has following toppings: ")
    for topping in toppings:
        print("- " + topping)


sand_wiches('a', 'b', 'c')
sand_wiches('d', 'g')
sand_wiches('e')