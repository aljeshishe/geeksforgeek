# https://practice.geeksforgeeks.org/problems/prefix-to-postfix-conversion/1?page=1&difficulty[]=1&sortBy=accuracy

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        OPS = "*/-+"
        stack = []
        for c in reversed(pre_exp):
            if c in OPS:
                left = stack.pop()
                right = stack.pop()
                stack.append(left + right + [c])
                continue
            stack.append([c])
        return "".join(stack[0])


# {
# Driver Code Starts.
def main():
    prefix = input()
    ob = Solution()
    res = ob.preToPost(prefix)
    print(res)
# } Driver Code Ends

import io
in_file = None
out_file = None
def input():
    global in_file
    return in_file.readline().strip()

_print = print
def print(*args, **kwargs):
    global out_file
    _print(*args, **kwargs, file=out_file, flush=True)

def test(input_text, expected):
    global in_file
    global out_file
    in_file = io.StringIO(input_text)
    out_file = io.StringIO()
    main()
    result = out_file.getvalue().strip()
    if result != expected:
        _print(f"{input_text}")
        _print(f"results!= expected\n{result=}\n{expected=}")
    else:
        _print("OK")
    return result

assert test("*-A/BC-/AKL", "ABC/-AK/L-*")