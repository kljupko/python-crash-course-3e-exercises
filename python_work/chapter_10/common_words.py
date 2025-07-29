from pathlib import Path

# Using the files from the lesson instead of the books. It still works.
filenames = [
    "cats.txt",
    "dogs.txt",
    "cats_and_dogs.py",
]

target_word = "the"

for filename in filenames:
    path = Path(filename)
    try:
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    else:
        word_count = content.lower().count(target_word)
        print(f"The word '{target_word}' appears about {word_count} "
              f"times in '{filename}'.")

