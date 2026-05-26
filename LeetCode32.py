# LeetCode32.py

def longestValidParentheses(s: str) -> int:
    """
    Calculates the length of the longest valid (well-formed) parentheses substring.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not s:
        return 0

    # Stack to store indices of parentheses.
    # -1 acts as the initial base boundary marker.
    stack = [-1]
    max_length = 0

    for i, char in enumerate(s):
        if char == "(":
            # Store the index of the opening parenthesis
            stack.append(i)
        else:
            # Pop the last opening parenthesis or base boundary
            stack.pop()

            if not stack:
                # If empty, this ')' is unmatched.
                # It becomes the new base boundary.
                stack.append(i)
            else:
                # If not empty, calculate the length of the valid match
                current_length = i - stack[-1]
                max_length = max(max_length, current_length)

    return max_length

def longestValidParenthesesV2(s : str) -> int:
    if not s:
        return 0
    max_len = 0
    stack = [-1]
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                len = i - stack[-1]    
                max_len = max(max_len, len)
    
    return max_len

if __name__ == "__main__":
    # Test cases: (input_string, expected_length)
    test_cases = [
        ("(()", 2),
        (")()())", 4),
        ("", 0),
        ("()()()", 6),
        ("(())", 4),
        ("()(()", 2),
        ("(()))())(", 4),
        # (")(f()())", 4),  # If your code handles non-parentheses or unmatched setups
        ("(((((", 0),
        ("))))", 0),
    ]

    print("Running Longest Valid Parentheses Practice Tests...\n")

    for s, expected in test_cases:
        # Call the function exactly once
        # actual = longestValidParentheses(s)
        actual = longestValidParenthesesV2(s)

        status = "✅ PASSED" if actual == expected else "❌ FAILED"

        print(f"[{status}]")
        print(f'  Input:    "{s}"')
        print(f"  Expected: {expected}")
        print(f"  Actual:   {actual}\n")
