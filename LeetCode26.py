from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """
    Removes duplicates from a sorted array in-place.
    Returns the number of unique elements (k).
    """
    if not nums:
        return 0

    # 'write_index' tracks where the next unique element should be placed
    write_index = 1

    # Iterate through the array starting from the second element
    for read_index in range(1, len(nums)):
        # If the current element is different from the previous one, it's unique
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1

    return write_index


def removeDuplicatesV2(nums: List[int]) -> int:
    n = len(nums)
    left = 0
    right = n
    uniqueNum = 0

    while left < right:
        # check duplicate number
        count = 0
        while left > 0 and left < right and nums[left] == nums[left - 1]:
            count += 1
            left += 1

        if count > 0:
            # move the rest to left
            for i in range(left - 1, right):
                nums[i - count] = nums[i]
            # check next number
            left = left - count
            right -= count
        else:
            left += 1

    return left


def removeDuplicatesV3(nums: List[int]) -> int:
    if not nums:
        return 0
    writeIndex = 1
    for readIndex in range(1, len(nums)):
        if nums[readIndex] != nums[readIndex - 1]:
            nums[writeIndex] = nums[readIndex]
            writeIndex += 1

    return writeIndex


# --- Updated Test Logic ---
if __name__ == "__main__":
    # Define multiple test cases
    # Format: (input_list, expected_k, expected_modified_prefix)
    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([], 0, []),
        ([1], 1, [1]),
        ([1, 1, 1, 1], 1, [1]),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
    ]

    print("Running test cases...")
    print("-" * 50)

    # Counters for pass/fail metrics
    passed_count = 0
    failed_count = 0

    for i, (nums, expected_k, expected_arr) in enumerate(test_cases):
        # Create a copy because the function modifies the list in-place
        nums_input = list(nums)

        # Call the implementation exactly once per test case
        # k = removeDuplicates(nums_input)
        # k = removeDuplicatesV2(nums_input)
        k = removeDuplicatesV3(nums_input)

        # Slice the modified array to check the first 'k' elements
        actual_arr = nums_input[:k]

        # Verify both the count and the modified prefix
        is_correct = (k == expected_k) and (actual_arr == expected_arr)

        if is_correct:
            passed_count += 1
            status = "PASSED"
        else:
            failed_count += 1
            status = "FAILED"

        print(f"Test Case {i + 1}: {status}")
        print(f"  Input:    {nums}")
        print(f"  Result k: {k} (Expected: {expected_k})")
        print(f"  Array:    {actual_arr} (Expected: {expected_arr})")
        print("-" * 50)

    # Final Summary Report
    print("\n================ TEST SUMMARY ================")
    print(f"Total Test Cases: {len(test_cases)}")
    print(f"Passed:           {passed_count}")
    print(f"Failed:           {failed_count}")
    print("==============================================")
