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


class IceCreamStand(Restaurant):
    """A simple attempt to model an ice cream stand."""

    def __init__(self, name, cuisine, flavors, served=0):
        """Initializes the attributes to describe an ice cream stand."""
        super().__init__(name, cuisine)
        self.flavors = flavors

    def list_flavors(self):
        """Prints all the flavors available."""
        print(f"Our offer at {self.restaurant_name.title()}:")
        for flavor in self.flavors:
            print(f" - {flavor.title()}")


flavors = ["chocolate", "vanilla", "strawberry", "mint", "rocky road"]
ice = IceCreamStand("fresh", "ice cream", flavors)
ice.list_flavors()
