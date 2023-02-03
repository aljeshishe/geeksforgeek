# https://practice.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1
#User function Template for python3
import sys


class Solution:


    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        result = []
        stack = []
        prio = {"^":4, "*":3, "/":3, "+":2, "-":2, "(":1}
        for c in exp:
            if c == "(":
                stack.append(c)
            elif c == ")":
                top = stack.pop()
                while top !="(":
                    result.append(top)
                    top = stack.pop()
            elif c in prio:
                while stack and prio[stack[-1]] >= prio[c]:
                    result.append(stack.pop())
                stack.append(c)
            else:
                result.append(c)

        while stack:
            result.append(stack.pop())

        return "".join(result)




#{
 # Driver Code Starts

def main(input):
    exp = str(input())
    ob=Solution()
    print(ob.InfixtoPostfix(exp))
# } Driver Code Ends




import io

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

assert test("a+b*(c^d-e)^(f+g*h)-i", "abcd^e-fgh*+^*+i-")