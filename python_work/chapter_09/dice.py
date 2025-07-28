from random import randint

class Die:
    """Represents a playing die for a boardgame."""
    def __init__(self, sides=6):
        """Initializes the attributes of the die."""
        self.sides = sides

    def roll_die(self):
        number = randint(1, self.sides)
        print(f"Rolled a {number}.")


die = Die()
for i in range(10):
    die.roll_die()
