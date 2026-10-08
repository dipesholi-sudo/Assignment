full_name = input("Enter your full name: ")

# split() with no arguments removes extra spaces, then join with underscores
username = "_".join(full_name.lower().split())
print("Username:", username)