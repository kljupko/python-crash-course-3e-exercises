from pathlib import Path
import json


def read_favorite_number(filename):
    """Reads the user's favorite number from the filename."""
    path = Path(filename)

    if path.exists():
        content = path.read_text(encoding="utf-8")
        num = json.loads(content)
        print(f"I know your favorite number! It's {num}.")
    else:
        num = get_favorite_number()
        store_favorite_number(num, filename)

def get_favorite_number():
    """Prompts the user for their favorite number and returns it."""
    while True:
        num = input("\nWhat's your favorite number? ")
        try:
            num = int(num)
        except ValueError:
            print("Please enter a valid number.")
        else:
            break
    return num

def store_favorite_number(number, filename):
    """Stores the given number in a file with the given filename."""
    path = Path(filename)
    content = json.dumps(number)
    path.write_text(content)
    print(f"\nNumber {number} written to file '{filename}'.")
    return True


filename = "favorite_number.json"
read_favorite_number(filename)
