import re

from typing import Literal, LiteralString,Any

def is_palindrome(sentence) -> bool:
    clean_sentence = re.sub(r'[^A-Za-z]', '', sentence).lower()
    return clean_sentence == clean_sentence[::-1]

# Sample usage
sentence = input("Enter a sentence: ")
if is_palindrome(sentence):
    print("Palindrome")
else:
    print("Not a palindrome")




def is_strong_password(password) -> tuple[Literal[False], Literal['Password must be at least 8 characters long']] | tuple[Literal[False], LiteralString] | tuple[Literal[False], LiteralString] | tuple[Literal[False], Literal['Password must contain at least one digit']] | tuple[Literal[False], LiteralString] | tuple[Literal[True], Literal['Password is strong']]:
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
valid, message = is_strong_password(password)
print(message)


def is_valid_email(email) -> bool:
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

# Sample usage
email: str = input("Enter an email address: ")
if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")




def capitalize_title(title) -> Any:
    
    capitalized_title = title.title()
    return capitalized_title

# Sample usage
title: str = input("Enter a title: ")
print("Capitalized Title:", capitalize_title(title))




def generate_acronym(phrase) -> LiteralString:
    words = phrase.split()
    # Exclude small words like 'and', 'of', 'the'
    small_words: list[str] = ['and', 'of', 'the']
    acronym: LiteralString = ''.join([word[0].upper() for word in words if word not in small_words])
    return acronym

# Sample usage
phrase = input("Enter a phrase: ")
print("Acronym:", generate_acronym(phrase))




def count_vowels_consonants(text) -> tuple[int, int]:
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_consonants = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    
    return num_vowels, num_consonants

# Sample usage
text: str = input("Enter a text: ")
vowels, consonants = count_vowels_consonants(text)
print(f"Vowels: {vowels}, Consonants: {consonants}")



from collections import Counter

def word_frequency(sentence) -> Counter[Any]:
    # Normalize the sentence (convert to lowercase and split into words)
    words = sentence.lower().split()
    # Use Counter to count word frequencies
    frequency = Counter(words)
    return frequency

# Sample usage
sentence: str = input("Enter a sentence: ")
frequency = word_frequency(sentence)
print("Word Frequencies:", frequency)

def reverse_words(sentence) -> LiteralString:
    # Split the sentence into words and reverse the order
    words = sentence.split()
    reversed_sentence: LiteralString = ' '.join(reversed(words))
    return reversed_sentence

# Sample usage
sentence = input("Enter a sentence: ")
print("Reversed Sentence:", reverse_words(sentence))



def is_valid_username(username) -> bool:
    # Check length of the username
    if len(username) < 5 or len(username) > 12:
        return False
    
    # Check if the username starts with an alphabetical letter
    if not username[0].isalpha():
        return False
    
    # Check if the username contains only letters, digits, and underscores
    if not re.match(r'^[A-Za-z0-9_]+$', username):
        return False
    
    return True

# Sample usage
username: str = input("Enter a username: ")
if is_valid_username(username):
    print("Valid Username")
else:
    print("Invalid Username")



# Username Validator
def is_valid_username_regex(username) -> bool:
    return re.match(r'^[A-Za-z][A-Za-z0-9_]{4,11}$', username) is not None

# Password Validator
def is_strong_password_regex(password) -> bool:
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_\-+=])[A-Za-z\d!@#$%^&*()_\-+=]{8,}$'
    return re.match(pattern, password) is not None




# Email Validator
def is_valid_email_regex(email) -> bool:
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Sample usage
username = input("Enter a username: ")
password = input("Enter a password: ")
email = input("Enter an email: ")

if is_valid_username_regex(username):
    print("Valid Username")
else:
    print("Invalid Username")

if is_strong_password_regex(password):
    print("Strong Password")
else:
    print("Weak Password")

if is_valid_email_regex(email):
    print("Valid Email")
else:
    print("Invalid Email")



def inventory_operations() -> None:
    inventory: list[str] = ['apple', 'banana', 'orange']
    
    # Add item to inventory
    inventory.append('grape')
    print("After adding 'grape':", inventory)
    
    # Remove item from inventory
    inventory.remove('banana')
    print("After removing 'banana':", inventory)
    
    # Sort the inventory
    inventory.sort()
    print("Sorted inventory:", inventory)
    
    # Count occurrences of an item
    count_apple: int = inventory.count('apple')
    print("Number of 'apple' in inventory:", count_apple)

# Sample usage
inventory_operations()




def manage_student_pairs() -> None:
    student_pairs = []
    
    while True:
        print("\nOptions: Add pair (1), Display pairs (2), Modify pair (3), Exit (4)")
        option = input("Choose an option: ")
        
        if option == '1':
            student1: str = input("Enter student 1 name: ")
            student2: str = input("Enter student 2 name: ")
            student_pairs.append((student1, student2))
        
        elif option == '2':
            print("Student pairs:", student_pairs)
        
        elif option == '3':
            index = int(input("Enter pair index to modify: "))
            student1 = input("Enter new student 1 name: ")
            student2 = input("Enter new student 2 name: ")
            student_pairs[index] = (student1, student2)
        
        elif option == '4':
            print("Exiting...")
            break

# Sample usage
manage_student_pairs()



def unique_orders() -> None:
    orders1: set[int] = {101, 102, 103, 104}
    orders2: set[int] = {103, 104, 105, 106}
    
    unique_orders: set[int] = orders1.union(orders2)
    print("Unique Orders:", unique_orders)

# Sample usage
unique_orders()



def sort_heights() -> None:
    participants: list[tuple[str, int]] = [("John", 170), ("Alice", 165), ("Bob", 180)]
    
    # Sort by height in descending order
    participants_sorted: list[tuple[str, int]] = sorted(participants, key=lambda x: x[1], reverse=True)
    
    print("Participants sorted by height:", participants_sorted)

# Sample usage
sort_heights()


