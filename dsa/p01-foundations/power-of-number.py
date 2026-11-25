"""
PrepInsta #39 · Power of a Number · Easy · P01 Foundations
https://prepinsta.com/interview-preparation/technical-interview-questions/most-asked-coding-questions-in-placements/
Task: Compute base raised to an integer power without using ** or pow().
Idea: Use binary exponentiation — recurse on power // 2, then square half (and multiply by base if power is odd).
Complexity: O(log |power|) time, O(log |power|) recursion stack space.
Gotchas: Negative powers flip to 1 / power_number(base, -power); 0 to a negative power raises ZeroDivisionError.
"""


def power_number(base: float, power: int) -> float:
    if power == 0:
        return 1
    if power < 0:
        return 1 / power_number(base, -power)

    half = power_number(base, power // 2)
    if power % 2 == 0:
        return half * half
    return base * half * half


if __name__ == "__main__":
    assert power_number(2, 0) == 1
    assert power_number(2, 5) == 32
    assert power_number(2, 10) == 1024
    assert power_number(2, -3) == 0.125
    assert power_number(-2, 3) == -8
    assert power_number(-2, 4) == 16
    print("ok")
