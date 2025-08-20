from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    """Represents the overall blog."""
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns a string representation of a blog."""
        return self.name.title()

class Post(models.Model):
    """Represents a single blog post."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of a blog post."""
        con = self.content
        if len(con) > 50:
            con = f"{con[:50]}..."
        return con