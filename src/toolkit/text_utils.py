def reverse_text(s):
    return s[::-1]


def is_palindrome(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


def count_words(s):
    return len(s.split())