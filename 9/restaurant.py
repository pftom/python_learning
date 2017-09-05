class Restaurant():
    """9-1 create a restaurant class

        Parameters:
            first_paramter: restaurant_name (str)
            second_paramter: cuisine_type (str)

        Return:
            class instance
    """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name)
        print("The restaurant cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print("I am opening!")


restaurant = Restaurant('weige', 'noodles')

print("The restaurant name is " + restaurant.restaurant_name)
print("The restaurant cuisine type is " + restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()