"""
PrepInsta #1 · Reverse a Number · Easy · P01 Foundations
https://prepinsta.com/interview-preparation/technical-interview-questions/most-asked-coding-questions-in-placements/
Task: Reverse the digits of an integer without converting it to a string.
Idea: Save the sign, take abs(num), then peel digits with % 10, build container * 10 + remainder, and shrink with // 10.
Complexity: O(log10 n) time, O(1) space.
Gotchas: Must take abs(num) before % and // for negatives (in Python, -123 % 10 == 7); trailing zeros drop (1200 -> 21).
"""


def reverse_number(num: int) -> int:
    sign = -1 if num < 0 else 1
    num = abs(num)
    container = 0

    while num > 0:
        remainder = num % 10
        container = (container * 10) + remainder
        num = num // 10

    return sign * container


if __name__ == "__main__":
    assert reverse_number(1234) == 4321
    assert reverse_number(1200) == 21
    assert reverse_number(0) == 0
    assert reverse_number(-123) == -321
    print("ok")
