"""
PrepInsta #3 · GCD of Two Numbers · Easy · P01 Foundations
https://prepinsta.com/interview-preparation/technical-interview-questions/most-asked-coding-questions-in-placements/
Task: Find the greatest common divisor (HCF) of two integers.
Idea: Brute force finds common divisors up to n1 and n2; Euclidean algorithm repeats a, b = b, a % b until b == 0.
Complexity: Brute force O(n1 + n2) time & space; Euclidean O(log min(|n1|, |n2|)) time, O(1) space.
Gotchas: Take abs() so negatives work; gcd(0, x) == |x| and gcd(0, 0) == 0 (brute force crashes on empty factors unless 0 is guarded).
"""


def gcd_brute(n1: int, n2: int) -> int:
    a, b = abs(n1), abs(n2)
    if a == 0:
        return b
    if b == 0:
        return a

    def factors(n: int) -> list[int]:
        return [i for i in range(1, n + 1) if n % i == 0]

    factor2 = set(factors(b))
    common = [f for f in factors(a) if f in factor2]
    return common[-1]


def gcd(n1: int, n2: int) -> int:
    a, b = abs(n1), abs(n2)
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    for fn in (gcd_brute, gcd):
        assert fn(48, 18) == 6
        assert fn(18, 48) == 6
        assert fn(7, 13) == 1
        assert fn(0, 5) == 5
        assert fn(0, 0) == 0
        assert fn(-12, 18) == 6
    print("ok")
