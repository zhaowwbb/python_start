def isPalindrome(x: int) -> bool:
    # Special cases:
    # 1. Negative numbers are not palindromes (e.g., -121)
    # 2. If the last digit is 0, the first digit must also be 0 (only '0' satisfies this)
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_number = 0
    # Reversing the second half of the number
    while x > reversed_number:
        pop = x % 10
        reversed_number = reversed_number * 10 + pop
        x //= 10

    # When the length is an odd number, we can get rid of the middle digit by reversed_number // 10
    return x == reversed_number or x == reversed_number // 10


def isPalindromeV2(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return 0
    reverse = 0
    while x > reverse:
        pop = x % 10
        reverse = reverse * 10 + pop
        x //= 10

    return x == reverse or x == reverse // 10


def run_tests():
    # Structured test case list referencing LeetCode 9 criteria
    test_cases = [
        {"input": 121, "expected": True, "desc": "Standard odd-length palindrome"},
        {"input": -121, "expected": False, "desc": "Negative number, not a palindrome"},
        {
            "input": 10,
            "expected": False,
            "desc": "Ends with 0 but is not 0, not a palindrome",
        },
        {"input": 0, "expected": True, "desc": "Single digit zero is a palindrome"},
        {"input": 7, "expected": True, "desc": "Single digit non-zero is a palindrome"},
        {"input": 123321, "expected": True, "desc": "Standard even-length palindrome"},
    ]

    print("Running LeetCode 9 - Palindrome Number Tests:\n" + "=" * 60)
    passed = 0

    for i, tc in enumerate(test_cases, 1):
        # Function is called exactly ONE time per iteration
        # result = isPalindrome(tc["input"])
        result = isPalindromeV2(tc["input"])        

        print(f"Test {i}: {tc['desc']}")
        print(f"  Input:    {tc['input']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Actual:   {result}")

        if result == tc["expected"]:
            print("  Status:   PASSED ✅")
            passed += 1
        else:
            print("  Status:   FAILED ❌")
        print("-" * 40)

    print(f"\nResult: {passed}/{len(test_cases)} tests passed.")


if __name__ == "__main__":
    run_tests()
