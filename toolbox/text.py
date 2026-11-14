"""Text helpers. The worked example every contribution is modelled on."""


def word_count(text):
    """Count whitespace-separated words.

    >>> word_count("one two three")
    3
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text.split())


def truncate(text, limit, suffix="..."):
    """Shorten text to limit characters, ending with suffix.

    The result is never longer than limit.

    >>> truncate("hello world", 8)
    'hello...'
    >>> truncate("short", 20)
    'short'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if limit < len(suffix):
        raise ValueError("limit must be at least len(suffix)")
    if len(text) <= limit:
        return text
    return text[:limit - len(suffix)] + suffix

def remove_extra_whitespace(text):
    """Remove unnecessary spaces from text."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return " ".join(text.split())

def character_count(text):
    """Count the total number of characters in text."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return len(text)

def reverse_text(text):
    """Reverse the given text.

    >>> reverse_text("hello")
    'olleh'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return text[::-1]


def count_vowels(text):
    """Count the number of vowels in text.

    >>> count_vowels("hello world")
    3
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    vowels = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count

# Testing all six helper functions

print("1. Word Count:", word_count("I love Python"))

print("2. Truncate:", truncate("Hello World Python", 8))

print("3. Remove Spaces:", remove_extra_whitespace("  Hello    World  "))

print("4. Character Count:", character_count("Hello World"))

print("5. Reverse Text:", reverse_text("Python"))

print("6. Count Vowels:", count_vowels("Hello World"))
