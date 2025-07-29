from pathlib import Path


path = Path("guest_book.txt")

prompt = "\n(press 'q' to quit)\n"
prompt += "What is your name? "

contents = ""

while True:
    name = input(prompt)

    if name.lower() == "q":
        break

    contents += f"{name}\n"
    print(f"Adding {name} to the guest book.")

path.write_text(contents)
print("Saved to guest_book.txt")
