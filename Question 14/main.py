# main.py
import string_utils

text = "hello"

print("Original:", text)
print("Reversed:", string_utils.reverse_string(text))
print("Capitalized:", string_utils.capitalize_string(text))
print("Uppercase:", string_utils.to_uppercase(text))
print("Lowercase:", string_utils.to_lowercase(text))
print("Is palindrome (level)?", string_utils.is_palindrome("level"))

#Output:
# Original: hello
# Reversed: olleh
# Capitalized: Hello
# Uppercase: HELLO
# Lowercase: hello
# Is palindrome (level)? True