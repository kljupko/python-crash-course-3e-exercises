"""Contains a class that represents a user of a website."""

class User:
    """A simple attempt to model a user profile."""

    def __init__(self, first_name, last_name, age, email):
        """Initialize the user profile attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User Profile:")
        print(f" - Name: {self.first_name.title()} {self.last_name.title()}")
        print(f" - Age: {self.age}")
        print(f" - Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting."""
        print(f"Hello, {self.first_name.title()}!\n")
