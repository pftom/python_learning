class Restaurant():
    """9-1  and 9-4 create a restaurant class

        Parameters:
            first_paramter: restaurant_name (str)
            second_paramter: cuisine_type (str)

        Return:
            class instance
    """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name)
        print("The restaurant cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print("I am opening!")

    def served_custom(self):
        print(str(self.number_served) + " customer have been served.")

    def set_number_served(self, num):
        if num >= 0:
            self.number_served = num
        else:
            print("You can't set the served num to negative")

    def increment_number_served(self, every_day_served_num):
        if every_day_served_num >= 0:
            self.number_served = self.number_served + every_day_served_num
        else:
            print("You can't increment with a negative!")


restaurant = Restaurant('weige', 'noodles')

print("The restaurant name is " + restaurant.restaurant_name)
print("The restaurant cuisine type is " + restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.served_custom()

restaurant.number_served = 3
restaurant.served_custom()

restaurant.set_number_served(8)
restaurant.served_custom()

restaurant.increment_number_served(9)
restaurant.served_custom()

restaurant.increment_number_served(-1)


# 9-6 extend restaurant 
class IceCreamStand(Restaurant):
    """create a icecream class"""
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """
        init super class attr
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_all_icecream(self):
        print("The restaurant has following flavors of icecream: ")
        flavors = self.flavors
        for icecream in flavors:
            print("- " + icecream)


my_icecream_store = IceCreamStand('Ancle Tom', 'IceCream', ['a', 'b'])
my_icecream_store.show_all_icecream()
