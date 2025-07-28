from random import randint, choice

def make_series():
    series = []

    num = randint(10, 99)
    while len(series) < 10 and num not in series:
        series.append(num)
        num = randint(10,99)
    
    series.extend(list("ABCDE"))

    return series

def make_ticket(series):
    ticket = []
    
    for i in range(4):
        ticket.append(choice(series))

    return ticket

series = make_series()
my_ticket = make_ticket(series)
print(f"My ticket: {my_ticket}")

counter = 0
while True:
    counter += 1
    winner = make_ticket(series)

    if my_ticket == winner:
        break

print(f"Winning tickt: {winner}")
print(f"And it only took {counter} attempts.")
