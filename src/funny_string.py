def funnyString(s):
    reverse = s[::-1]
    string_diff = []
    for i in range(len(s) - 1):
        string_diff.append(abs(ord(s[i]) - ord(s[i + 1])))
    reverse_diff = []
    for i in range(len(reverse) - 1):
        reverse_diff.append(abs(ord(reverse[i]) - ord(reverse[i + 1])))
    if string_diff == reverse_diff:
        return "Funny"
    else:
        return "Not Funny"
