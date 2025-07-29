from pathlib import Path


filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    path = Path(filename)
    try:
        content = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"\nContents of {filename}:")
        for line in content.splitlines():
            print(f" - {line.strip()}")
