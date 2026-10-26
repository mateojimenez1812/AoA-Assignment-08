"""
Analysis of Algorithms - Assignment 08
Exercise 2: ComparisonCountingSort
Exercise 3: DistributionCountingSort and comparison between both algorithms
"""
import random
import time


def comparison_counting_sort(A, counter=None):
    """
    Sorts A by counting, for each element, how many elements are smaller than it.
    That count is the final position of the element in the sorted array.
    Time: Theta(n^2) (always n(n-1)/2 comparisons).  Extra space: Theta(n).
    """
    n = len(A)
    count = [0] * n
    for i in range(n - 1):
        for j in range(i + 1, n):
            if counter is not None:
                counter[0] += 1
            if A[i] < A[j]:
                count[j] += 1
            else:
                count[i] += 1
    S = [None] * n
    for i in range(n):
        S[count[i]] = A[i]
    return S


def distribution_counting_sort(A, low, high, counter=None):
    """
    Sorts A whose values are integers in the range [low, high].
    1) Count the frequency of each value.
    2) Turn the frequencies into a cumulative distribution.
    3) Place each element at its final position (right to left, so it is stable).
    Time: Theta(n + k), with k = high - low + 1.  Extra space: Theta(n + k).
    """
    n = len(A)
    k = high - low + 1
    D = [0] * k
    for i in range(n):                 # frequencies
        D[A[i] - low] += 1
        if counter is not None:
            counter[0] += 1
    for j in range(1, k):              # cumulative distribution
        D[j] += D[j - 1]
        if counter is not None:
            counter[0] += 1
    S = [None] * n
    for i in range(n - 1, -1, -1):     # place elements
        j = A[i] - low
        S[D[j] - 1] = A[i]
        D[j] -= 1
        if counter is not None:
            counter[0] += 1
    return S


if __name__ == "__main__":
    print("EXERCISE 2: ComparisonCountingSort")
    A = [62, 31, 84, 96, 19, 47]
    print("Input  :", A)
    print("Output :", comparison_counting_sort(A))

    random.seed(8)
    ok = 0
    for _ in range(500):
        L = [random.randint(-100, 100) for _ in range(random.randint(0, 80))]
        if comparison_counting_sort(L) == sorted(L):
            ok += 1
    print(f"{ok}/500 random lists sorted correctly (compared with sorted())")

    print()
    print("EXERCISE 3: DistributionCountingSort")
    B = [13, 11, 12, 13, 12, 12]
    print("Input  :", B, "  (values between 11 and 13)")
    print("Output :", distribution_counting_sort(B, 11, 13))

    ok = 0
    for _ in range(500):
        L = [random.randint(0, 50) for _ in range(random.randint(0, 200))]
        if distribution_counting_sort(L, 0, 50) == sorted(L):
            ok += 1
    print(f"{ok}/500 random lists sorted correctly (compared with sorted())")

    print("\nComparison of both algorithms (random values between 0 and 99):")
    print(f"{'n':>7} {'ComparisonCounting':>20} {'DistributionCounting':>22} {'CC time (s)':>12} {'DC time (s)':>12}")
    print(f"{'':>7} {'(comparisons)':>20} {'(basic operations)':>22}")
    for n in [100, 500, 1000, 2000, 4000]:
        L = [random.randint(0, 99) for _ in range(n)]
        c1, c2 = [0], [0]
        t0 = time.perf_counter(); comparison_counting_sort(L, c1); t1 = time.perf_counter()
        distribution_counting_sort(L, 0, 99, c2); t2 = time.perf_counter()
        print(f"{n:>7} {c1[0]:>20} {c2[0]:>22} {t1 - t0:>12.4f} {t2 - t1:>12.4f}")
    print("-> ComparisonCounting grows as n(n-1)/2 (quadratic);")
    print("   DistributionCounting grows as 2n + k (linear in n for a fixed range k).")
