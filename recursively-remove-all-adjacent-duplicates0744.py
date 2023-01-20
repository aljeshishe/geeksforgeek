import dataclasses


@dataclasses.dataclass
class Item:
    char: str
    count: int


#
# def f(s):
#     q = deque()
#     for c in s:
#         # check empty
#         if not q:
#             q.append(Item(char=c, count=1))
#             continue
#
#         if q[-1].char != c:
#             if q[-1].count > 1:
#                 q.pop()
#
#         if q[-1].char == c:
#             q[-1].count += 1
#         else:
#             q.append(Item(char=c, count=1))
#     return "".join(item.char for item in q)

def func(s):
    res, pos = f(s, pos=0)
    return "".join(res)
# loop
    # get char
    # if char is same increment counter, contione
    # if char is differnet
        # already have duplicates
            # return
        # no duplictes
            # call recursivelly get result and pos
def f(s, pos):
    result = []
    c = Item(char=s[pos], count=1)
    pos += 1
    while pos < len(s):
        if s[pos] != c.char:
            res, pos = f(s=s, pos=pos)
            result += res
        else:
            c.count += 1
        pos += 1

    if c.count > 1:
        return result, pos
    else:
        return [c.char] + result, pos


def log(v):
    print(v)
    return v


#assert log(func("geeksforgeek")) == "gksforgk"
assert log(func("abccbccba")) == ""
