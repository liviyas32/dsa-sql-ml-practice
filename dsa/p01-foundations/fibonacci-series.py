"""
PrepInsta #2 · Fibonacci Series Up to n Terms · Easy · P01 Foundations
https://prepinsta.com/interview-preparation/technical-interview-questions/most-asked-coding-questions-in-placements/
Task: Return the first n terms of the Fibonacci sequence starting from 0, 1.
Idea: Track the rolling pair (a, b) = (0, 1); append a and advance via tuple unpacking a, b = b, a + b for n steps.
Complexity: O(n) time, O(n) output space (O(1) auxiliary space).
Gotchas: Guard num <= 0 to return []; return a list instead of printing inside the function so callers and asserts can use the result.
"""


def fibonacci_series(num: int) -> list[int]:
    if num <= 0:
        return []

    output_term: list[int] = []
    a, b = 0, 1
    for _ in range(num):
        output_term.append(a)
        a, b = b, a + b
    return output_term


if __name__ == "__main__":
    assert fibonacci_series(0) == []
    assert fibonacci_series(-3) == []
    assert fibonacci_series(1) == [0]
    assert fibonacci_series(2) == [0, 1]
    assert fibonacci_series(6) == [0, 1, 1, 2, 3, 5]
    print("ok")
