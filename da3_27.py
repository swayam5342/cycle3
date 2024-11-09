
character_book_data: list[tuple[str, str]] = [("Harry", "Harry Potter"), ("Hermione", "Harry Potter"), ("Frodo", "LOTR")]

book_characters:dict = {}
for character, book in character_book_data:
    book_characters.setdefault(book, set()).add(character)

print("Characters by book:", book_characters)
