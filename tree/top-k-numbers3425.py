# https://practice.geeksforgeeks.org/problems/top-k-numbers3425/1
# User function Template for python3
from collections import defaultdict


class Solution:
    def kTop(self, a, n, k):
        results = []
        pairs = []
        d = defaultdict(int)
        for value in a:
            old = d[value]
            d[value] = old + 1
            try:
                pairs.remove((old, -value))
            except ValueError:
                pass
            pairs.append((d[value], -value))

            for pos in range(len(pairs) - 2, -1, -1):
                if pairs[pos] < pairs[pos + 1]:
                    pairs[pos], pairs[pos + 1] = pairs[pos + 1], pairs[pos]

            if len(pairs) > k:
                pairs.pop()
            results += [-pair[1] for pair in pairs]
        return results


# {
# Driver Code Starts
# Initial Template for Python 3


def main(input):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ob = Solution()
    ans = ob.kTop(a, n, k)
    print(*ans)

# } Driver Code Ends    def __init__(self, value, item):


import io, sys

def test(input_text, expected):
    global input
    old_stdout = sys.stdout
    stdout = sys.stdout = io.StringIO()

    try:
        main(input=iter(io.StringIO(input_text)).__next__)
    finally:
        sys.stdout = old_stdout

    result = stdout.getvalue().strip()
    if result != expected:
        print(f"{input_text}")
        print(f"results!= expected\n{result=}\n{expected=}")
    else:
        print("OK")
    return result

i = """5 4
5 2 1 3 2"""
assert test(i, "5 2 5 1 2 5 1 2 3 5 2 1 3 5")