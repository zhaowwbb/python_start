import sys


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        n = len(s)

        for i in range(n):
            current_val = roman_map[s[i]]

            # If the current value is less than the next value, subtract it
            if i < n - 1 and current_val < roman_map[s[i + 1]]:
                total -= current_val
            else:
                total += current_val

        return total

    def romanToIntV2(self, s: str) -> int:
        romanValueMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        n = len(s)

        for i in range(n):
            currentValue = romanValueMap[s[i]]
            if i < n - 1 and currentValue < romanValueMap[s[i + 1]]:
                total -= currentValue
            else:
                total += currentValue

        return total

    def romanToIntV3(self, s: str) ->int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            } 
        total = 0
        n = len(s)
        for i in range(n):
            currentVal = roman_map[s[i]]
            if i < n - 1 and currentVal < roman_map[s[i+1]]:
                total -= currentVal
            else:
                total += currentVal
                
        return total            

def run_tests():
    solution = Solution()

    # Test cases: { input_roman_string: expected_integer }
    test_cases = {
        # LeetCode Examples
        "III": 3,
        "LVIII": 58,
        "MCMXCIV": 1994,
        "MMMDCCXLIX": 3749,
        # Single Base Symbols
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        # Subtractive Forms
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
        # Upper Boundary Constraint Complement
        "MMMCMXCIX": 3999,
    }

    passed_count = 0
    failed_count = 0
    total_cases = len(test_cases)

    print(f"{'INPUT':<15} | {'EXPECTED':<10} | {'ACTUAL':<10} | {'STATUS'}")
    print("-" * 60)

    for roman, expected in test_cases.items():
        # The implementation is invoked exactly once per test case
        # actual = solution.romanToInt(roman)
        # actual = solution.romanToIntV2(roman)
        actual = solution.romanToIntV3(roman)        

        if actual == expected:
            status = "PASS"
            passed_count += 1
        else:
            status = f"FAIL (Expected {expected}, got {actual})"
            failed_count += 1

        print(f"{roman:<15} | {expected:<10} | {actual:<10} | {status}")

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
