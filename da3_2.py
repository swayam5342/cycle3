import re
from typing import  Literal

def is_strong_password(password) -> tuple[Literal[False],str] | tuple[Literal[True],str]:
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit"
    
    if not re.search(r'[!@#$%^&*()_\-+=]', password):
        return False, "Password must contain at least one special character (!@#$%^&*()_-+=)"
    
    return True, "Password is strong"

# Sample usage
password: str = input("Enter a password: ")
valid , message = is_strong_password(password)
print(message)