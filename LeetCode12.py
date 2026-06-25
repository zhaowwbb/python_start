import sys


class Solution:
    def intToRoman(self, num: int) -> str:
        # Map values to their Roman numeral symbols in descending order
        value_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        roman_segments = []
        for value, symbol in value_map:
            if num == 0:
                break
            count = num // value
            if count > 0:
                roman_segments.append(symbol * count)
                num %= value

        return "".join(roman_segments)

    def intToRomanV2(self, num: int) -> str:
        value_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        roman_segments = []
        for value, symbol in value_map:
            if num == 0:
                break
            count = num // value
            roman_segments.append(count * symbol)
            num %= value

        return "".join(roman_segments)

    def intToRomanV3(self, num: int) -> str:
        value_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        roman_segments = []
        for value, symbol in value_map:
            if num == 0:
                break
            count = num // value
            roman_segments.append(count * symbol)
            num %= value

        return "".join(roman_segments)


def run_tests():
    solution = Solution()

    # Test cases: { input_integer: expected_roman_string }
    test_cases = {
        # LeetCode Examples
        3749: "MMMDCCXLIX",
        58: "LVIII",
        1994: "MCMXCIV",
        # Boundary Constraints
        1: "I",
        3999: "MMMCMXCIX",
        # Subtractive Forms
        4: "IV",
        9: "IX",
        40: "XL",
        90: "XC",
        400: "CD",
        900: "CM",
        # Base Symbols
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }

    passed_count = 0
    failed_count = 0
    total_cases = len(test_cases)

    print(f"{'INPUT':<10} | {'EXPECTED':<15} | {'ACTUAL':<15} | {'STATUS'}")
    print("-" * 60)

    for num, expected in test_cases.items():
        # The implementation is invoked exactly once per test case
        # actual = solution.intToRoman(num)
        # actual = solution.intToRomanV2(num)
        actual = solution.intToRomanV3(num)

        if actual == expected:
            status = "PASS"
            passed_count += 1
        else:
            status = f"FAIL (Expected {expected}, got {actual})"
            failed_count += 1

        print(f"{num:<10} | {expected:<15} | {actual:<15} | {status}")

    print("-" * 60)
    print(f"Execution Summary:")
    print(f"Total Test Cases: {total_cases}")
    print(f"PASSED          : {passed_count}")
    print(f"FAILED          : {failed_count}")
    print("-" * 60)

    if failed_count == 0:
        print("Result: ALL TESTS PASSED")
        sys.exit(0)
    else:
        print("Result: SOME TESTS FAILED")
        sys.exit(1)


if __name__ == "__main__":
    run_tests()
