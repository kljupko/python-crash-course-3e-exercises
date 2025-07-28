class User:
    """A simple attempt to model a user profile."""

    def __init__(self, first_name, last_name, age, email):
        """Initialize the user profile attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User Profile:")
        print(f" - Name: {self.first_name.title()} {self.last_name.title()}")
        print(f" - Age: {self.age}")
        print(f" - Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting."""
        print(f"Hello, {self.first_name.title()}!")

    def increment_login_attempts(self):
        """Increases the login_attempts attribute."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the login_attempts attribute back to 0."""
        self.login_attempts = 0


user = User("guy", "some", 20, "some.guy@example.com")

for i in range(14):
    user.increment_login_attempts()
print(user.login_attempts)
print()

user.reset_login_attempts()
print(user.login_attempts)
