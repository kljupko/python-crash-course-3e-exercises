from pathlib import Path
import json

def get_stored_user_data(path):
    """Get stored user data if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

def get_new_user_data(path):
    """Prompt for new user data."""
    user = {}
    user['username'] = input("What is your name? ")
    user['age'] = input("What is your age? ")
    user['email'] = input("What is your email? ")
    contents = json.dumps(user)
    path.write_text(contents)
    return user

def greet_user():
    """Greet the user by name."""
    path = Path('user.json')
    user = get_stored_user_data(path)
    if user:
        print(f"Welcome back, {user['username']}!")
    else:
        user = get_new_user_data(path)
        print(f"We'll remember this about you:")
        for key, value in user.items():
            print(f" - {key.title()}: {value}")

greet_user()
