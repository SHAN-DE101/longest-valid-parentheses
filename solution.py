def longest_valid_parentheses(s: str) -> int:
    """Return the length of the longest valid (well-formed) parentheses substring."""
    max_len = 0

    # Pass 1: Left-to-right scan
    left = right = 0
    for ch in s:
        if ch == "(":
            left += 1
        else:
            right += 1

        if left == right:
            max_len = max(max_len, 2 * right)
        elif right > left:
            left = right = 0

    # Pass 2: Right-to-left scan
    left = right = 0
    for ch in reversed(s):
        if ch == "(":
            left += 1
        else:
            right += 1

        if left == right:
            max_len = max(max_len, 2 * left)
        elif left > right:
            left = right = 0

    return max_len
