"""
PrepInsta #28 · ASCII Value of a Character · Easy · P01 Foundations
https://prepinsta.com/interview-preparation/technical-interview-questions/most-asked-coding-questions-in-placements/
Task: Return the ASCII (Unicode code point) value of each character in a string or single character.
Idea: Map Python's built-in ord() over the characters directly via a list comprehension.
Complexity: O(n) time, O(n) output space (O(1) for a single character).
Gotchas: ord() returns Unicode code points (identical to ASCII for 0-127); anchors: '0'=48, 'A'=65, 'a'=97; inverse is chr().
"""


def ascii_value(word: str) -> list[int]:
    return [ord(w) for w in word]


if __name__ == "__main__":
    assert ascii_value("A") == [65]
    assert ascii_value("a") == [97]
    assert ascii_value("0") == [48]
    assert ascii_value("Hi") == [72, 105]
    assert ascii_value("") == []
    print("ok")
