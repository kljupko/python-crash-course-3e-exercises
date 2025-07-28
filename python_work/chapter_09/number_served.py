class Restaurant:
    """A simple attempt to model a resaurant."""
    def __init__(self, name, cuisine, served=0):
        """Initialize the attributes to describe a restaurant."""
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = served

    def describe_restaurant(self):
        """Return a neatly formatted restaurant description."""
        desc = f"The {self.restaurant_name.title()} restaurant serves"
        desc += f" {self.cuisine_type.title()} food."
        print(desc)

    def open_restaurant(self):
        """Returns a sting stating that the restaurant is open."""
        print(f"The {self.restaurant_name.title()} restaurant is open!")

    def set_number_served(self, number):
        """Sets the number_served attribute."""
        self.number_served = number
    
    def increment_number_served(self, number):
        """Increases the number_served attribute."""
        self.number_served += number


rest = Restaurant("marina", "mediterranian")
print(rest.number_served)
rest.number_served = 17
print(rest.number_served)
print()

rest.set_number_served(30)
print(rest.number_served)
print()

rest.increment_number_served(14)
print(rest.number_served)
