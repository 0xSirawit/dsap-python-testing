def gridChallenge(grid: list) -> str:
    grid = [list(row) for row in grid]
    n = len(grid)
    for i in range(n):
        grid[i].sort()
    for col in range(len(grid[0])):
        for row in range(1, n):
            if grid[row][col] < grid[row - 1][col]:
                return "NO"
    return "YES"
