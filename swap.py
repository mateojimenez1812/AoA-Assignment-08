"""
Analysis of Algorithms - Assignment 08
Exercise 1: Exchange the values of two variables u and v without extra storage
"""


def swap_arithmetic(u, v):
    """Swap using addition and subtraction (no temporary variable)."""
    u = u + v      # u now holds the sum
    v = u - v      # (u + v) - v = original u
    u = u - v      # (u + v) - original u = original v
    return u, v


def swap_xor(u, v):
    """Swap using bitwise XOR (integers only, no temporary variable)."""
    u = u ^ v
    v = u ^ v      # (u ^ v) ^ v = original u
    u = u ^ v      # (u ^ v) ^ original u = original v
    return u, v


if __name__ == "__main__":
    print("EXERCISE 1: Swapping two variables without extra storage")

    print("\nMethod 1: addition and subtraction")
    u, v = 7, 15
    print(f"Before: u = {u}, v = {v}")
    u = u + v
    print(f"  u = u + v  ->  u = {u}, v = {v}")
    v = u - v
    print(f"  v = u - v  ->  u = {u}, v = {v}")
    u = u - v
    print(f"  u = u - v  ->  u = {u}, v = {v}")
    print(f"After:  u = {u}, v = {v}")

    print("\nMethod 2: bitwise XOR")
    u, v = 12, 25
    print(f"Before: u = {u} ({u:05b}), v = {v} ({v:05b})")
    u = u ^ v
    print(f"  u = u ^ v  ->  u = {u} ({u:05b}), v = {v} ({v:05b})")
    v = u ^ v
    print(f"  v = u ^ v  ->  u = {u} ({u:05b}), v = {v} ({v:05b})")
    u = u ^ v
    print(f"  u = u ^ v  ->  u = {u} ({u:05b}), v = {v} ({v:05b})")
    print(f"After:  u = {u}, v = {v}")

    print("\nMore tests:")
    tests = [(3, 9), (-4, 10), (0, 5), (100, -100), (8, 8), (2.5, 7.25)]
    for a, b in tests:
        r1 = swap_arithmetic(a, b)
        r2 = swap_xor(a, b) if isinstance(a, int) and isinstance(b, int) else "n/a (floats)"
        print(f"  u = {a}, v = {b}  ->  arithmetic: {r1}   xor: {r2}")

    print("\nAnswer: Yes, it is possible. Both methods use only u and v, no extra variable.")
    print("Note: the arithmetic method may overflow with fixed-size integers (e.g. in C/C++),")
    print("and the XOR method only works with integers.")
