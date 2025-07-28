"""
Contains a set of classes that represent a web admin and their privileges.
"""

from user_module import User

class Admin(User):
    """A special user with administrative privileges."""

    def __init__(self, first_name, last_name, age, email, privileges):
        """Initialize attributes of the parent class and privileges."""
        super().__init__(first_name, last_name, age, email)
        self.privileges = privileges


class Privileges:
    """Specifies the privileges of an administrator."""
    def __init__(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges of the administrator."""
        print(f"Administrator Privileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")
