# https://practice.geeksforgeeks.org/problems/...
import heapq


def f(grid):
    rows_n = len(grid)
    cols_n = len(grid[0])
    dist = grid[rows_n - 1][cols_n - 1]
    q = [(dist, rows_n - 1, cols_n - 1)]
    dists = [[1000000] * cols_n for _ in range(rows_n)]

    while q:
        top = heapq.heappop(q)
        top_dist, row, col = top

        steps = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]
        for nrow, ncol in steps:
            if 0 <= nrow < rows_n and 0 <= ncol < cols_n:
                dist = grid[nrow][ncol] + top_dist
                if dist < dists[nrow][ncol]:
                    dists[nrow][ncol] = dist
                    heapq.heappush(q, (dist, nrow, ncol))

    return dists[0][0]


def log(v):
    print(v)
    return v


def make_grid(text):
    res = [list(map(int, line.strip().split())) for line in list(text.split("\n"))[1:]]
    return res


input = """4
9 4 9 9 
6 7 6 4 
8 3 3 7 
7 4 9 10"""
assert log(f(make_grid(input))) == result
assert log(f(make_grid(input))) == result
