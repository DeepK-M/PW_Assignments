# A module for basic string manipulation utilities

def reverse_string(s: str) -> str:
    """Return the reversed version of the string"""
    return s[::-1]

def capitalize_string(s: str) -> str:
    """Return the string with the first character capitalized"""
    return s.capitalize()

def to_uppercase(s: str) -> str:
    """Return the string in uppercase"""
    return s.upper()

def to_lowercase(s: str) -> str:
    """Return the string in lowercase"""
    return s.lower()

def is_palindrome(s: str) -> bool:
    """Check if the string is a palindrome"""
    return s == s[::-1]
