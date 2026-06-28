# ==========================================
# 1. IMPLEMENTATION
# ==========================================
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if an input string containing brackets is valid.
        Uses a stack data structure to track opening brackets.
        """
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top element if stack is not empty, else use a dummy value
                top_element = stack.pop() if stack else "#"

                # If the mapping doesn't match the popped element, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly
        return len(stack) == 0

    def isValidV2(self, s: str) -> bool:
        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in bracket_map:
                top_element = stack.pop() if stack else "#"
                if top_element != bracket_map[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

    def isValidV3(self, s: str) -> bool:
        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in bracket_map:
                top_element = stack.pop() if stack else "#"
                if top_element != bracket_map[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0


# ==========================================
# 2. TEST LOGIC
# ==========================================
def run_tests():
    solution = Solution()

    # Test cases defined as (input_string, expected_boolean_output)
    test_cases = [
        ("()", True),  # Standard matching pair
        ("()[]{}", True),  # Multiple distinct matching pairs
        ("(]", False),  # Mismatched closing bracket
        ("([)]", False),  # Incorrect nesting/interleaved pairs
        ("{[]}", True),  # Correctly nested pairs
        ("(", False),  # Single opening bracket (unclosed)
        ("]", False),  # Single closing bracket (nothing to pop)
        ("", True),  # Empty string (technically valid structurally)
    ]

    success_count = 0
    failed_count = 0

    print("Executing Test Cases...\n" + "-" * 40)

    for i, (input_str, expected) in enumerate(test_cases, 1):
        # Call the implementation exactly once per test case
        # result = solution.isValid(input_str)
        # result = solution.isValidV2(input_str)
        result = solution.isValidV3(input_str)

        if result == expected:
            print(f"Test Case {i}: PASSED")
            success_count += 1
        else:
            print(
                f"Test Case {i}: FAILED (Input: '{input_str}' | Expected: {expected} | Got: {result})"
            )
            failed_count += 1

    print("-" * 40)
    print(f"SUMMARY: {success_count} passed, {failed_count} failed.")


if __name__ == "__main__":
    run_tests()
