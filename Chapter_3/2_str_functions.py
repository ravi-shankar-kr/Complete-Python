# name = "Harry"

# print(len(name))
# print(name.endswith("rry"))
# print(name.startswith("Ha"))
# print(name.capitalize())

# Sample string
text = "  Hello World! Welcome to Python 101.  "

print("Original String:")
print(repr(text))
print()

# 1. Length of string
print("Length:", len(text))

# 2. Lowercase
print("Lowercase:", text.lower())

# 3. Uppercase
print("Uppercase:", text.upper())

# 4. Strip (remove leading and trailing spaces)
print("Strip:", text.strip())

# 5. Left Strip
print("LStrip:", text.lstrip())

# 6. Right Strip
print("RStrip:", text.rstrip())

# 7. Split into list
print("Split:", text.split())

# 8. Join a list into string
words = ['Hello', 'Python', 'World']
print("Join:", "-".join(words))

# 9. Replace substring
print("Replace:", text.replace("Python", "Java"))

# 10. Find a substring
print("Find 'World':", text.find("World"))

# 11. Count occurrences
print("Count 'o':", text.count("o"))

# 12. Startswith
print("Startswith '  Hello':", text.startswith("  Hello"))

# 13. Endswith
print("Endswith '101.  ':", text.endswith("101.  "))

# 14. Capitalize
print("Capitalize:", text.strip().capitalize())

# 15. Title case
print("Title:", text.title())

# 16. Check isalpha
print("'Hello' isalpha:", "Hello".isalpha())

# 17. Check isdigit
print("'12345' isdigit:", "12345".isdigit())

# 18. Check isalnum
print("'abc123' isalnum:", "abc123".isalnum())

# 19. Zfill
print("'42' zfilled to 5:", "42".zfill(5))
