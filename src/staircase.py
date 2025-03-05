def staircase(n: int, pattern: chr) -> str:
    return "\n".join((" " * (n - i)) + (pattern * i) for i in range(1, n + 1))
