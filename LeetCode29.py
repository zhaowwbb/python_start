import sys


def divide(dividend: int, divisor: int) -> int:
    """
    Divides two integers without using multiplication, division, or mod operators.
    Clamps the result to a 32-bit signed integer range.
    """
    # Define 32-bit signed integer bounds
    MAX_INT = 2147483647  # 2^31 - 1
    MIN_INT = -2147483648  # -2^31

    # Handle overflow edge cases
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT
    if dividend == MIN_INT and divisor == 1:
        return MIN_INT

    # Determine the sign of the result
    # True if one and only one input is negative
    is_negative = (dividend < 0) ^ (divisor < 0)

    # Use absolute values for the calculation
    abs_dividend = abs(dividend)
    abs_divisor = abs(divisor)

    quotient = 0

    # Perform bit-shifting division
    while abs_dividend >= abs_divisor:
        temp_divisor = abs_divisor
        multiple = 1

        # Keep doubling the divisor and multiple while it fits in the dividend
        while abs_dividend >= (temp_divisor << 1):
            temp_divisor <<= 1
            multiple <<= 1

        # Subtract the largest found multiple and update the quotient
        abs_dividend -= temp_divisor
        quotient += multiple

    # Apply sign and clamp within 32-bit bounds
    result = -quotient if is_negative else quotient
    return max(MIN_INT, min(MAX_INT, result))


def divideV2(dividend: int, divisor: int) -> int:
    # MIN_INT = -2^31
    # MAX_INT = 2^31 - 1
    MAX_INT = 2147483647  # 2^31 - 1
    MIN_INT = -2147483648  # -2^31

    if dividend == MIN_INT and divisor == -1:
        return MAX_INT
    if dividend == MIN_INT and divisor == 1:
        return MIN_INT

    isNegative = (dividend < 0) ^ (divisor < 0)
    absDividend = abs(dividend)
    absDivisor = abs(divisor)

    quotient = 0
    while absDividend >= absDivisor:
        tempDivisor = absDivisor
        multiple = 1
        while absDividend > tempDivisor << 1:
            tempDivisor <<= 1
            multiple <<= 1

        absDividend -= tempDivisor
        quotient += multiple

    if quotient > MAX_INT:
        return MAX_INT
    if quotient < MIN_INT:
        return MIN_INT
    if isNegative:
        return -quotient
    else:
        return quotient


def divideV3(dividend: int, divisor: int) -> int:
    MAX_INT = 2147483647  # 2^31 - 1
    MIN_INT = -2147483648  # -2^31

    if dividend == MIN_INT and divisor == -1:
        return MAX_INT
    if dividend == MIN_INT and divisor == 1:
        return MIN_INT

    isNegative = (dividend < 0) ^ (divisor < 0)
    abs_dividend = abs(dividend)
    abs_divisor = abs(divisor)

    quotient = 0
    while abs_dividend >= abs_divisor:
        tempDivisor = abs_divisor
        multiple = 1
        while abs_dividend > tempDivisor << 1:
            tempDivisor <<= 1
            multiple <<= 1
        abs_dividend -= tempDivisor
        quotient += multiple

    if quotient > MAX_INT:
        return MAX_INT
    if quotient < MIN_INT:
        return MIN_INT
    if isNegative:
        return -quotient
    else:
        return quotient


# --- Test Logic ---
if __name__ == "__main__":
    # 32-bit bounds for test validation
    MAX_INT = 2147483647
    MIN_INT = -2147483648

    # Define multiple test cases
    # Format: (dividend, divisor, expected_quotient)
    test_cases = [
        (10, 3, 3),
        (7, -3, -2),
        (0, 1, 0),
        (1, 1, 1),
        (-1, 1, -1),
        (100, 7, 14),
        # Overflow / Edge Cases
        (MIN_INT, -1, MAX_INT),
        (MIN_INT, 1, MIN_INT),
        (MAX_INT, 1, MAX_INT),
    ]

    print("Running test cases for Divide Two Integers...")
    print("-" * 50)

    # Counters for metrics
    passed_count = 0
    failed_count = 0

    for i, (dividend, divisor, expected) in enumerate(test_cases):
        # Call the implementation exactly once per test case
        # result = divide(dividend, divisor)
        # result = divideV2(dividend, divisor)
        result = divideV3(dividend, divisor)

        is_correct = result == expected

        if is_correct:
            passed_count += 1
            status = "PASSED"
        else:
            failed_count += 1
            status = "FAILED"

        print(f"Test Case {i + 1}: {status}")
        print(f"  Dividend: {dividend} | Divisor: {divisor}")
        print(f"  Result:   {result} (Expected: {expected})")
        print("-" * 50)

    # Final Summary Report
    print("\n================ TEST SUMMARY ================")
    print(f"Total Test Cases: {len(test_cases)}")
    print(f"Passed:           {passed_count}")
    print(f"Failed:           {failed_count}")
    print("==============================================")
