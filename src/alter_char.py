def alternatingCharacters(s: str) -> int:
    del_n = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            del_n += 1

    return del_n
