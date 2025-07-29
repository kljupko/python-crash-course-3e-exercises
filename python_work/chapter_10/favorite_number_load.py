from pathlib import Path
import json

filename = "favorite_number.json"
path = Path(filename)
try:
    content = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
else:
    num = json.loads(content)
    print(f"I know your favorite number! It's {num}.")
