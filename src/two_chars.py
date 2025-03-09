def twoChars(s: str) -> int:
    u_chars = set(s)

    max_len = 0
    for char1 in u_chars:
        for char2 in u_chars:
            if char1 == char2:
                continue
            filtered = [c for c in s if c == char1 or c == char2]
            is_alter = True
            for i in range(1, len(filtered)):
                if filtered[i] == filtered[i - 1]:
                    is_alter = False
                    break
            if is_alter and len(filtered) > 0:
                max_len = max(max_len, len(filtered))

    return max_len
