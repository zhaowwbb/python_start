def strStr(haystack: str, needle: str) -> int:
    """
    Finds the index of the first occurrence of needle in haystack.
    Returns -1 if needle is not part of haystack.
    """
    # Edge case: An empty needle is always found at index 0
    if not needle:
        return 0

    n, m = len(haystack), len(needle)

    # Only iterate up to the point where the remaining haystack is at least as long as needle
    for i in range(n - m + 1):
        # Check if the substring matches the needle
        if haystack[i : i + m] == needle:
            return i

    return -1


def strStrV2(haystack: str, needle: str) -> int:
    if len(haystack) < len(needle):
        return -1
    result = -1
    n = len(haystack)
    for i in range(n):
        isMatch = True
        for j in range(len(needle)):
            if i + j < n and needle[j] == haystack[i + j]:
                continue
            else:
                isMatch = False
                break
        if isMatch:
            return i

    return result


def strStrV3(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    m, n = len(haystack), len(needle)
    for i in range(m - n + 1):
        if haystack[i : i + n] == needle:
            return i

    return -1


# --- Test Logic ---
if __name__ == "__main__":
    # Define multiple test cases
    # Format: (haystack, needle, expected_index)
    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("hello", "ll", 2),
        ("a", "a", 0),
        ("abc", "", 0),
        ("mississippi", "issip", 4),
    ]

    print("Running test cases for Find First Occurrence...")
    print("-" * 50)

    # Counters for metrics
    passed_count = 0
    failed_count = 0

    for i, (haystack, needle, expected_index) in enumerate(test_cases):
        # Call the implementation exactly once per test case
        # result = strStr(haystack, needle)
        # result = strStrV2(haystack, needle)
        result = strStrV3(haystack, needle)        

        is_correct = result == expected_index

        if is_correct:
            passed_count += 1
            status = "PASSED"
        else:
            failed_count += 1
            status = "FAILED"

        print(f"Test Case {i + 1}: {status}")
        print(f"  Haystack: '{haystack}' | Needle: '{needle}'")
        print(f"  Result Index: {result} (Expected: {expected_index})")
        print("-" * 50)

    # Final Summary Report
    print("\n================ TEST SUMMARY ================")
    print(f"Total Test Cases: {len(test_cases)}")
    print(f"Passed:           {passed_count}")
    print(f"Failed:           {failed_count}")
    print("==============================================")
