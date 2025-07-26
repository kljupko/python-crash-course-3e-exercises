usernames = ["admin", "sam", "strider", "legoblocks", "gimme"]

if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin! Would you like to see the status report?")
        else:
            print(f"Hello {user}! Thank you for logging in again.")
else:
    print("We need to find some users!")


# no users
usernames = []

if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin! Would you like to see the status report?")
        else:
            print(f"Hello {user}! Thank you for logging in again.")
else:
    print("We need to find some users!")
