from pathlib import Path
import json

while True:
    num = input("What is your favorite number? ")

    try:
        num = int(num)
    except ValueError:
        print("Please enter a number.")
    else:
        content = json.dumps(num)
        filename = "favorite_number.json"
        path = Path(filename)
        path.write_text(content)
        print(f"Stored number to '{filename}'")
        break
