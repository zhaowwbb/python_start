from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generates all combinations of well-formed parentheses.
        Uses a backtracking approach.
        """
        result = []

        def backtrack(current_str: str, open_count: int, close_count: int):
            # Base case: If the current string reaches the maximum length (2 * n)
            if len(current_str) == 2 * n:
                result.append(current_str)
                return

            # If we can still add an opening parenthesis, do so
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)

            # If we have more opening than closing parentheses, we can add a closing one
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result

    def generateParenthesisV2(self, n: int) -> list[str]:
        result = []

        def backtrack(s: str, leftCount: int, rightCount: int):
            if len(s) == 2 * n:
                result.append(s)
                return

            if leftCount < n:
                backtrack(s + "(", leftCount + 1, rightCount)

            if rightCount < leftCount:
                backtrack(s + ")", leftCount, rightCount + 1)

        backtrack("", 0, 0)
        return result

    def generateParenthesisV3(self, n: int) -> list[str]:
        result = []

        def backtrack(s: str, openCount: int, closeCount: int):
            if len(s) == 2 * n:
                result.append(s)
                return

            if openCount < n:
                backtrack(s + "(", openCount + 1, closeCount)
            if closeCount < openCount:
                backtrack(s + ")", openCount, closeCount + 1)

        backtrack("", 0, 0)
        return result


# ==========================================
# TEST LOGIC
# ==========================================
if __name__ == "__main__":
    solution = Solution()

    # Define test cases: (input_n, expected_output)
    # Note: LeetCode output order doesn't strictly matter, so we sort arrays to compare them reliably.
    test_cases = [
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (0, [""]),
        (
            4,
            [
                "(((())))",
                "((()()))",
                "((())())",
                "((()))()",
                "(()(()))",
                "(()()())",
                "(()())()",
                "(())(())",
                "(())()()",
                "()((()))",
                "()(()())",
                "()(())()",
                "()()(())",
                "()()()()",
            ],
        ),
    ]

    success_count = 0
    failed_count = 0

    print("Running Tests...")
    print("-" * 50)

    for i, (n, expected) in enumerate(test_cases):
        # Generate the result from the implementation
        # actual = solution.generateParenthesis(n)
        # actual = solution.generateParenthesisV2(n)
        actual = solution.generateParenthesisV3(n)

        # Sort both lists to ensure order mismatches don't falsely fail the test
        sorted_actual = sorted(actual)
        sorted_expected = sorted(expected)

        if sorted_actual == sorted_expected:
            print(f"Test Case {i + 1} (n={n}): PASSED")
            success_count += 1
        else:
            print(f"Test Case {i + 1} (n={n}): FAILED")
            print(f"  Expected: {sorted_expected}")
            print(f"  Got:      {sorted_actual}")
            failed_count += 1

    print("-" * 50)
    print(f"Total Successes: {success_count}")
    print(f"Total Failures:  {failed_count}")
