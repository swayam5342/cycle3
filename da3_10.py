import re

def is_valid_username(username) -> bool:
    return re.match(r'^[A-Za-z][A-Za-z0-9_]{4,11}$', username) is not None




username: str = input("Enter a username: ")
if is_valid_username(username):
    print("Valid Username")
else:
    print("Invalid Username")