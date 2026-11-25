"""
PrepInsta #11 · Leap Year Check · Easy · P01 Foundations
https://prepinsta.com/interview-preparation/technical-interview-questions/most-asked-coding-questions-in-placements/
Task: Check whether a given year is a leap year.
Idea: Divisible by 4 and not 100, or divisible by 400.
Complexity: O(1) time, O(1) space.
Gotchas: Century years like 1900 are NOT leap years unless divisible by 400 (2000); use logical `and`, never bitwise `&` (which binds tighter than `==`).
"""


def leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


if __name__ == "__main__":
    assert leap_year(2024) is True   # regular leap year
    assert leap_year(2000) is True   # century divisible by 400
    assert leap_year(1900) is False  # century not divisible by 400
    assert leap_year(2023) is False  # regular non-leap year
    print("ok")
