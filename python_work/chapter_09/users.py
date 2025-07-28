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
        print(f"Hello, {self.first_name.title()}!")


user1 = User("guy", "some", 20, "some.guy@example.com")
user2 = User("john", "doe", 30, "john.doe@example.com")
user3 = User("jane", "doe", 55, "jane.doe@example.com")

user1.describe_user()
user1.greet_user()
print()

user2.describe_user()
user2.greet_user()
print()

user3.describe_user()
user3.greet_user()
