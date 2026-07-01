from typing import List


def removeElement(nums: List[int], val: int) -> int:
    """
    Removes all occurrences of val in nums in-place.
    Returns the number of elements which are not equal to val (k).
    """
    # write_index tracks where the next non-val element should be placed
    write_index = 0

    # Loop through all elements in the array
    for read_index in range(len(nums)):
        # If the current element is not equal to the target value
        if nums[read_index] != val:
            nums[write_index] = nums[read_index]
            write_index += 1

    return write_index


def removeElementV2(nums: List[int], val: int) -> int:
    if not nums:
        return 0
    writeIndex = 0
    for readIndex in range(len(nums)):
        if nums[readIndex] != val:
            nums[writeIndex] = nums[readIndex]
            writeIndex += 1

    return writeIndex


def removeElementV3(nums: List[int], val: int) -> int:
    writeIndex = 0
    for readIndex in range(len(nums)):
        if nums[readIndex] != val:
            nums[writeIndex] = nums[readIndex]
            writeIndex += 1

    return writeIndex


# --- Test Logic ---
if __name__ == "__main__":
    # Define multiple test cases
    # Format: (input_list, target_val, expected_k, expected_elements)
    # Note: LeetCode accepts the first k elements in any order.
    test_cases = [
        ([3, 2, 2, 3], 3, 2, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
        ([], 1, 0, []),
        ([1], 1, 0, []),
        ([1], 2, 1, [1]),
        ([2, 2, 2], 2, 0, []),
    ]

    print("Running test cases for Remove Element...")
    print("-" * 50)

    # Counters for metrics
    passed_count = 0
    failed_count = 0

    for i, (nums, val, expected_k, expected_arr) in enumerate(test_cases):
        # Create a deep copy of the input list to preserve the original for printing
        nums_input = list(nums)

        # Call the implementation exactly once per test case
        # k = removeElement(nums_input, val)
        # k = removeElementV2(nums_input, val)
        k = removeElementV3(nums_input, val)

        # Slice out the first k elements modified by the function
        actual_arr = nums_input[:k]

        # LeetCode accepts elements in any order, so we sort both arrays to verify contents
        is_correct = (k == expected_k) and (sorted(actual_arr) == sorted(expected_arr))

        if is_correct:
            passed_count += 1
            status = "PASSED"
        else:
            failed_count += 1
            status = "FAILED"

        print(f"Test Case {i + 1}: {status}")
        print(f"  Input Array: {nums} | Target Value: {val}")
        print(f"  Result k:    {k} (Expected: {expected_k})")
        print(f"  Array:       {actual_arr} (Expected elements: {expected_arr})")
        print("-" * 50)

    # Final Summary Report
    print("\n================ TEST SUMMARY ================")
    print(f"Total Test Cases: {len(test_cases)}")
    print(f"Passed:           {passed_count}")
    print(f"Failed:           {failed_count}")
    print("==============================================")
