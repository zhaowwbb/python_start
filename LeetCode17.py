def letterCombinations(digits: str) -> list[str]:
    """
    Returns all possible letter combinations that the number could represent.
    Time Complexity: O(4^N * N) | Space Complexity: O(N) for the recursion stack.
    """
    if not digits:
        return []

    # Map digits to their corresponding letters (exactly like a phone keypad)
    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    combinations = []

    def backtrack(index: int, path: list[str]):
        # Base case: If the current path is as long as the input digits, we found a combination
        if len(path) == len(digits):
            combinations.append("".join(path))
            return

        # Get the letters corresponding to the current digit
        current_digit = digits[index]
        possible_letters = phone_map[current_digit]

        for letter in possible_letters:
            path.append(letter)  # Step 1: Choose a letter
            backtrack(index + 1, path)  # Step 2: Recurse to the next digit
            path.pop()  # Step 3: Backtrack (remove the letter)

    # Start the backtracking process from index 0 with an empty path
    backtrack(0, [])
    return combinations


def letterCombinationsV2(digits: str) -> list[str]:
    if len(digits) == 0:
        return []
    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    combinations = []

    def backtrack(index: int, path: list[str]):
        if len(path) == len(digits):
            combinations.append("".join(path))
            return

        current_digit = digits[index]
        possible_letters = phone_map[current_digit]

        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return combinations


def letterCombinationsV3(digits: str) -> list[str]:
    if len(digits) == 0:
        return []
    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    combinations = []

    def backtrack(index: int, path: list[str]):
        if len(path) == len(digits):
            combinations.append("".join(path))
            return
        digit_index = digits[index]
        possible_letters = phone_map[digit_index]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return combinations


def run_test_suite():
    # Define test cases: sets are used for 'expected' to ignore order matching variations
    test_cases = [
        {
            "name": "Standard LeetCode Example",
            "digits": "23",
            "expected": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        },
        {"name": "Empty Input String", "digits": "", "expected": []},
        {"name": "Single Digit Input", "digits": "2", "expected": ["a", "b", "c"]},
        {
            "name": "Digits with 4 Letters (7 and 9)",
            "digits": "7",
            "expected": ["p", "q", "r", "s"],
        },
        {
            "name": "Longer Combination Mix",
            "digits": "234",
            "expected": [
                "adg",
                "adh",
                "adi",
                "aeg",
                "aeh",
                "aei",
                "afg",
                "afh",
                "afi",
                "bdg",
                "bdh",
                "bdi",
                "beg",
                "beh",
                "bei",
                "bfg",
                "bfh",
                "bfi",
                "cdg",
                "cdh",
                "cdi",
                "ceg",
                "ceh",
                "cei",
                "cfg",
                "cfh",
                "cfi",
            ],
        },
        # Intentionally adding a failing test case to demonstrate failure counting logic
        # {
        #     "name": "Deliberate Failure Case",
        #     "digits": "2",
        #     "expected": ["x", "y", "z"]
        # }
    ]

    passed_count = 0
    failed_count = 0

    print("=" * 70)
    print(f"{'RUNNING LETTER COMBINATIONS TEST SUITE':^70}")
    print("=" * 70)

    for i, tc in enumerate(test_cases, 1):
        # The implementation is called exactly ONCE per test case here
        # actual = letterCombinations(tc["digits"])
        # actual = letterCombinationsV2(tc["digits"])
        actual = letterCombinationsV3(tc["digits"])

        # Convert lists to sets to ensure matching ignores element ordering rules
        if set(actual) == set(tc["expected"]):
            passed_count += 1
            status = "✅ PASSED"
            details = f"Generated {len(actual)} combinations"
        else:
            failed_count += 1
            status = "❌ FAILED"
            details = f"Expected {len(tc['expected'])} items, got {len(actual)}"

        print(f"Test {i}: {tc['name']:<38} | {status} ({details})")

    print("-" * 70)
    print(f"TOTAL PASSED: {passed_count}")
    print(f"TOTAL FAILED: {failed_count}")
    print(f"SUCCESS RATE: {(passed_count / len(test_cases)) * 100:.1f}%")
    print("=" * 70)


# Run the unified script
if __name__ == "__main__":
    run_test_suite()
