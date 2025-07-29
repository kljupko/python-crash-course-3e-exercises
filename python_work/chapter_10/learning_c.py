from pathlib import Path

path = Path("learning_python.txt")

content = path.read_text().rstrip()
lines = content.splitlines()
for line in lines:
    line = line.replace("Python", "C")
    print(line)
