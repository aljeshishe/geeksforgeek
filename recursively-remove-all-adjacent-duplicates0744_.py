def removeDuplicates(s, ch):
    if s is None or len(s) <= 1:
        return s

    i, j = 0, 0
    while i < len(s):

        if i + 1 < len(s) and s[i] == s[i + 1]:
            j = i

            while j + 1 < len(s) and s[j] == s[j + 1]:
                j += 1

            if i > 0:
                lastChar = s[i - 1]
            else:
                lastChar = ch

            remStr = removeDuplicates(s[j + 1:], lastChar)

            s = s[0: i]

            while len(remStr) > 0 and len(s) > 0 and remStr[0] == s[len(s) - 1]:

                while len(remStr) > 0 and remStr[0] != ch and remStr[0] == s[len(s) - 1]:
                    remStr = remStr[1: len(remStr)]

                s = s[0: len(s) - 1]

            s = s + remStr
            i = j

        else:
            i += 1

    return s
def f(s):
    return removeDuplicates(s, " ")

def log(v):
    print(v)
    return v


assert log(f("geeksforgeek")) == "gksforgk"
assert log(f("abccbccbad")) == "d"
