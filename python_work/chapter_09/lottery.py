from random import randint, choice

def make_series():
    series = []

    num = randint(10, 99)
    while len(series) < 10 and num not in series:
        series.append(num)
        num = randint(10,99)
    
    series.extend(list("ABCDE"))

    return series

def make_winner(series):
    winner = []
    
    for i in range(4):
        winner.append(choice(series))

    return winner

series = make_series()
winner = make_winner(series)

print(f"Winning ticket: {winner}")
