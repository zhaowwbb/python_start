class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Iterate through the characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Check this character against the rest of the strings
            for string in strs[1:]:
                # If the current string is shorter than i, or characters don't match
                if i == len(string) or string[i] != char:
                    return strs[0][:i]

        return strs[0]

    def longestCommonPrefixV2(self, strs: list[str]) -> str:
        result = []
        if not strs:
            return ""
        firstStr = strs[0]

        if len(strs) == 1:
            return firstStr

        for i in range(len(firstStr)):
            currentChar = firstStr[i]

            # for string in strs[1:]:
            for j in range(1, len(strs)):
                nextStr = strs[j]
                if i == len(nextStr) or nextStr[i] != currentChar:
                    # return strs[0][:i]
                    return "".join(result)
                    # break
            result.append(currentChar)

        return strs[0]

    def longestCommonPrefixV3(self, strs: list[str]) -> str:
        if not strs:
            return ""
        first = strs[0]
        for i in range(len(first)):
            currentChar = first[i]
            for string in strs[1:]:
                if i == len(string) or currentChar != string[i]:
                    return first[:i]
        return first


def run_tests():
    solution = Solution()

    # Define test cases: (input_data, expected_output)
    test_cases = [
        (["flower", "flow", "flight"], "fl"),  # Case 1: Standard match
        (["dog", "racecar", "car"], ""),  # Case 2: No match
        (["interstate", "interview", "internal"], "inter"),  # Case 3: Partial match
        (["alone"], "alone"),  # Case 4: Single element
        (["", "b", "c"], ""),  # Case 5: Contains empty string
        (["test", "test", "test"], "test"),  # Case 6: Identical strings
        ([], ""),  # Case 7: Empty list
    ]

    passed_count = 0
    failed_count = 0

    print("--- Running LeetCode 14 Tests ---")

    for index, (inputs, expected) in enumerate(test_cases, start=1):
        # The implementation is called exactly once per test case here
        # result = solution.longestCommonPrefix(inputs)
        # result = solution.longestCommonPrefixV2(inputs)
        result = solution.longestCommonPrefixV3(inputs)

        if result == expected:
            print(f"Test Case {index}: PASSED")
            passed_count += 1
        else:
            print(f"Test Case {index}: FAILED (Expected '{expected}', got '{result}')")
            failed_count += 1

    print("---------------------------------")
    print(f"Summary: {passed_count} passed, {failed_count} failed.")


if __name__ == "__main__":
    run_tests()
