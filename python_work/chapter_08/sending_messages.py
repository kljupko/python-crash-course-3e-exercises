messages = ["hi!", "hello!", "who goes there!"]
sent_messages = []

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)


send_messages(messages)
print()

print("Messages:")
print(messages)

print("\nSent messages:")
print(sent_messages)

