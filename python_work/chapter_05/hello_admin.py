usernames = ["admin", "sam", "strider", "legoblocks", "gimme"]

for user in usernames:
    if user == "admin":
        print("Hello admin! Would you like to see the status report?")
    else:
        print(f"Hello {user}! Thank you for logging in again.")
