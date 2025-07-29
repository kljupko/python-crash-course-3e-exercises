from pathlib import Path


print("file_reader.py")
path = Path("pi_digits.txt")
contents = path.read_text()

for line in contents.splitlines():
    print(line)


print("\npi_string.py")
path = Path("pi_digits.txt")
contents = path.read_text()

pi_string = ""

for line in contents.splitlines():
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


print("\npi_birthday.py")
path = Path("pi_million_digits.txt")
contents = path.read_text()

pi_string = ""

for line in contents.splitlines():
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears to be in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
