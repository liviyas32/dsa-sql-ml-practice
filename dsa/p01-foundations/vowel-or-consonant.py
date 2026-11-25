"""
PrepInsta #26 · Vowel or Consonant · Easy · P01 Foundations
https://prepinsta.com/interview-preparation/technical-interview-questions/most-asked-coding-questions-in-placements/
Task: Classify each character in a string (or single character) as a vowel, consonant, or invalid letter.
Idea: Lowercase the input, iterate characters directly, check English letters with isascii() & isalpha(), and test membership in a vowel set.
Complexity: O(n) time, O(n) output space (O(1) for a single character).
Gotchas: Strings are already iterable (no list() copy needed); use a set for O(1) lookup; isalpha() alone matches non-ASCII Unicode letters.
"""


def character(word: str) -> list[str]:
    vowels = {"a", "e", "i", "o", "u"}
    output_char = []

    for c in word.lower():
        if c.isascii() and c.isalpha():
            if c in vowels:
                output_char.append("Vowel")
            else:
                output_char.append("Consonant")
        else:
            output_char.append("Invalid letter")

    return output_char


if __name__ == "__main__":
    assert character("A") == ["Vowel"]
    assert character("z") == ["Consonant"]
    assert character("5") == ["Invalid letter"]
    assert character("Hi!") == ["Consonant", "Vowel", "Invalid letter"]
    assert character("") == []
    print("ok")
