"""
PrepInsta #38 · Sum of Digits of a Number · Easy · P01 Foundations
https://prepinsta.com/interview-preparation/technical-interview-questions/most-asked-coding-questions-in-placements/
Task: Return the sum of all digits of an integer.
Idea: Take abs(num), repeatedly add num % 10 to a running total, and drop the last digit with num // 10.
Complexity: O(log10 n) time, O(1) space.
Gotchas: Take abs(num) first so negative inputs don't skip the while num > 0 loop; 0 returns 0.
"""


def sum_digit(num: int) -> int:
    num = abs(num)
    add = 0

    while num > 0:
        remainder = num % 10
        add += remainder
        num = num // 10

    return add


if __name__ == "__main__":
    assert sum_digit(1234) == 10
    assert sum_digit(0) == 0
    assert sum_digit(-456) == 15
    assert sum_digit(7) == 7
    print("ok")
