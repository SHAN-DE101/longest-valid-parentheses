from solution import longest_valid_parentheses


def test_examples() -> None:
    assert longest_valid_parentheses("(()") == 2
    assert longest_valid_parentheses(")()())") == 4
    assert longest_valid_parentheses("") == 0


def test_edge_cases() -> None:
    assert longest_valid_parentheses("()") == 2
    assert longest_valid_parentheses("(())") == 4
    assert longest_valid_parentheses("()(()") == 2
    assert longest_valid_parentheses(")()(()))") == 6
    assert longest_valid_parentheses("(((") == 0
    assert longest_valid_parentheses(")))") == 0
    assert longest_valid_parentheses("(" * 15000 + ")" * 15000) == 30000
