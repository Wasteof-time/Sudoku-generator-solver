import random
n=9

def solve_sudoku(grid):
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 0:
                numbers = list(range(1, n + 1))
                random.shuffle(numbers)
                for num in numbers:
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def generate_full():
    grid= [[0]*9 for _ in range(9)]
    solve_sudoku(grid)
    return grid