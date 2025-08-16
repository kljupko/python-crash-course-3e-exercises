# Update the Entry __str__ method to add elipsis...
#   only if the entry is longer than 50 characters.

# The method would look like this.
def __str__(self):
    """Return a simple string representing the entry."""
    if (len(self.text) > 50):
        return f"{self.text[:50]}..."
    else:
        return self.text