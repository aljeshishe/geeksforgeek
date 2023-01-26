# https://practice.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1

# User function Template for python3

class Solution:

    # Function to find a solved Sudoku.
    def SolveSudoku(self, grid):
        self.l = len(grid)
        arr = grid
        self.sets1 = [{arr[row][col] for col in range(self.l) if arr[row][col]} for row in range(self.l)]
        self.sets2 = [{arr[row][col] for row in range(self.l) if arr[row][col]} for col in range(self.l)]
        self.sets3 = [[set() for _ in range(self.l // 3)] for _ in range(self.l // 3)]
        subl = self.l // 3
        for qrow in range(subl):
            for qcol in range(subl):
                items = set()
                for row in range(subl):
                    for col in range(subl):
                        r = qrow * 3 + row
                        c = qcol * 3 + col
                        item = arr[r][c]
                        if item:
                            items.add(item)
                self.sets3[qrow][qcol] = items
        return self.f(grid, pos=0)

    # Function to print grids of the Sudoku.
    def printGrid(self, arr):
        for row in range(self.l):
            for col in range(self.l):
                print(arr[row][col], end=" ")

    def f(self, arr, pos):
        for npos in range(pos + 1, self.l * self.l):
            row, col = divmod(npos, self.l)
            if arr[row][col] == 0:
                break
        else:
            return True

        candidates = set(range(1, 10)) - self.sets1[row] - self.sets2[col] - self.sets3[row // 3][col // 3]
        for i in candidates:
            arr[row][col] = i
            self.sets1[row].add(i)
            self.sets2[col].add(i)
            self.sets3[row // 3][col // 3].add(i)

            if self.f(arr, pos):
                return True

            arr[row][col] = 0
            self.sets1[row].remove(i)
            self.sets2[col].remove(i)
            self.sets3[row // 3][col // 3].remove(i)

        return False


# {
# Driver Code Starts
# Initial Template for Python 3


def make_grid(input):
    items = input.split()
    pos = 0
    grid = []
    for row in range(9):
        row = []
        for col in range(9):
            row.append(int(items[pos]))
            pos += 1
        grid.append(row)
    return grid
ob = Solution()

i = "3 0 6 5 0 8 4 0 0 5 2 0 0 0 0 0 0 0 0 8 7 0 0 0 0 3 1 0 0 3 0 1 0 0 8 0 9 0 0 8 6 3 0 0 5 0 5 0 0 9 0 6 0 0 1 3 0 0 0 0 2 5 0 0 0 0 0 0 0 0 7 4 0 0 5 2 0 6 3 0 0"
grid = make_grid(i)
if (ob.SolveSudoku(grid) == True):
    ob.printGrid(grid)
    print()
else:
    print("No solution exists")
# } Driver Code Ends
