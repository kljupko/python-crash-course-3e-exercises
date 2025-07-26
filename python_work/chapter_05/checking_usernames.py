current_users = ["admin", "sam", "strider", "LEGOblocks", "Gimme"]
new_users = ["mary", "poppin", "fredo", "LegoBlocks", "GIMME"]

current_lower = []
for user in current_users:
    current_lower.append(user.lower())

for user in new_users:
    if user.lower() in current_lower:
        print(f"{user}, you will need to enter a new username.")
    else:
        print(f"The username {user} is available.")
