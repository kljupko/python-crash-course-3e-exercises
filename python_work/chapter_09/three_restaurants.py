class Restaurant:
    """A simple attempt to model a resaurant."""
    def __init__(self, name,cuisine):
        """Initialize the attributes to describe a restaurant."""
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        """Return a neatly formatted restaurant description."""
        desc = f"The {self.restaurant_name.title()} restaurant serves"
        desc += f" {self.cuisine_type.title()} food."
        print(desc)

    def open_restaurant(self):
        """Returns a sting stating that the restaurant is open."""
        print(f"The {self.restaurant_name.title()} restaurant is open!")

marina = Restaurant("marina", "mediterranian")
seigi = Restaurant("seigi", "japanese")
forest = Restaurant("forest", "vegeterian")

marina.describe_restaurant()
seigi.describe_restaurant()
forest.describe_restaurant()
