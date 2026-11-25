"""
PrepInsta #46 · Factorial (Recursion) · Easy · P01 Foundations
https://prepinsta.com/interview-preparation/technical-interview-questions/most-asked-coding-questions-in-placements/
Task: Compute n! recursively for a non-negative integer n.
Idea: Base case 0! = 1! = 1; otherwise return num * fact_recursive(num - 1).
Complexity: O(n) time, O(n) recursion stack space.
Gotchas: Negative inputs recurse infinitely unless guarded with ValueError; large n (~1000+) hits Python's recursion limit (use iterative for large n).
"""


def fact_recursive(num: int) -> int:
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if num == 0 or num == 1:
        return 1
    return num * fact_recursive(num - 1)


if __name__ == "__main__":
    assert fact_recursive(0) == 1
    assert fact_recursive(1) == 1
    assert fact_recursive(5) == 120
    assert fact_recursive(6) == 720
    try:
        fact_recursive(-1)
        assert False, "Expected ValueError for negative input"
    except ValueError:
        pass
    print("ok")
