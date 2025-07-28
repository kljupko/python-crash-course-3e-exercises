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


class Admin(User):
    """A special user with administrative privileges."""

    def __init__(self, first_name, last_name, age, email, privileges):
        """Initialize attributes of the parent class and privileges."""
        super().__init__(first_name, last_name, age, email)
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges of the administrator."""
        print(f"Administrator Privileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")


admin_privileges = [
    "can add post",
    "can delete post",
    "can ban user",
    "can reset passwords",
    ]

admin = Admin("admin", "omeragić", 37,
              "admin.omeragic@example.com",
              admin_privileges)
admin.describe_user()
admin.show_privileges()
