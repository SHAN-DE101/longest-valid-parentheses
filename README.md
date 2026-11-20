# Longest Valid Parentheses

Given a string `s` containing just `'('` and `')'`, returns the length of the longest valid (well-formed) parentheses substring.

## Approach
Two-pass linear scan (left-to-right and right-to-left) tracking opening and closing counts:
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
