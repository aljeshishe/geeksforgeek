# User function Template for python3
import io


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.key}:{self.value}"

    __repr__ = __str__


class LRUCache:
    # head and tail always point to Node()
    # tail.prev = last item
    # head.next - first item
    # Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap: int):
        self.cap = cap
        node = Node()
        self.tail = self.head = node.next = node.prev = node
        self.d = dict()
        self.counter = 0

    def get(self, key):
        node = self.d.get(key)
        if node is None:
            return -1

        self._remove(node)
        self._append(node)

        return node.value

    def set(self, key, value):
        node = self.d.get(key)
        if node:
            self._remove(node)

        node = Node(key=key, value=value)
        self._append(node)
        self.d[key] = node

        if self.counter > self.cap:
            node = self._pop_tail()
            del self.d[node.key]

    def _pop_tail(self):
        to_remove = self.tail.prev
        self._remove(to_remove)
        return to_remove

    def _remove(self, node):
        assert self.counter > 0
        self.counter -= 1
        node.prev.next = node.next
        node.next.prev = node.prev

    @staticmethod
    def _connect(left, right):
        left.next = right
        right.prev = left

    def _append(self, node):
        self.counter += 1
        self._connect(node, self.head.next)
        self._connect(self.head, node)


# {
# Driver Code Starts
# Initial Template for Python 3
text = """2
21
SET 89 88 GET 67 GET 85 GET 18 GET 61 SET 6 38 SET 19 18 SET 74 84 GET 74 SET 84 90 SET 58 79 GET 72 SET 60 1 GET 39 SET 75 89 SET 82 58 SET 71 59 SET 40 18 SET 23 64 GET 74 SET 63 32"""
file = io.StringIO(text)
def input():
    global file
    return file.readline().strip()

if __name__ == '__main__':
    cap = int(input())  # capacity of the cache
    qry = int(input())  # number of queries
    a = list(map(str, input().strip().split()))  # parent child info in list

    lru = LRUCache(cap)

    i = 0
    q = 1
    while q <= qry:
        qtyp = a[i]

        if qtyp == 'SET':
            lru.set(int(a[i + 1]), int(a[i + 2]))
            i += 3
        elif qtyp == 'GET':
            print(lru.get(int(a[i + 1])), end=' ')
            i += 2
        q += 1
    print()
# } Driver Code Ends