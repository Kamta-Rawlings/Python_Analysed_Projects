'''
A finite string can be interpreted as an infinite
sequence of characters by wrapping around at the
start and end of the string. Indeed, the character
past the last character in the string becomes the
first character, and the character before the first
character is the last character in the string.
As an example, consider
the string “word” (consisting of 4 characters):
'''


def create_sequence(s, start, count):
    """Return `count` characters from the infinite wrap-around sequence of s,
    starting at index `start` (start may be negative)."""
    result = ""          # 1
    n = len(s)           # 2

    for i in range(count):              # 3
        real_index = (start + i) % n   # 4
        result += s[real_index]        # 5

    return result         # 6


'''
Understand the question well.
The first thing is to understand the word repeats itself
multiple times.
Then use the mode operation to pick the numbers position
'''
