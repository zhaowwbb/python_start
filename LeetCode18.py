def fourSum(nums: list[int], target: int) -> list[list[int]]:
    """
    Finds all unique quadruplets in the array which gives the sum of target.
    Time Complexity: O(N^3) | Space Complexity: O(1) (excluding output storage)
    """
    nums.sort()
    results = []
    n = len(nums)

    # First pointer
    for i in range(n - 3):
        # Skip duplicates for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Pruning optimization 1: Minimum possible sum is too large
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        # Pruning optimization 2: Maximum possible sum with this i is too small
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue

        # Second pointer
        for j in range(i + 1, n - 2):
            # Skip duplicates for the second number
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # Pruning optimization 3: Minimum possible sum here is too large
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            # Pruning optimization 4: Maximum possible sum here is too small
            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                continue

            # Two-pointer framework for the remaining two numbers
            left = j + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    results.append([nums[i], nums[j], nums[left], nums[right]])

                    # Move pointers past any duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return results


def fourSumV2(nums: list[int], target: int) -> list[list[int]]:
    if len(nums) < 4:
        return []
    nums.sort()
    result = []
    length = len(nums)
    for i in range(length - 4):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, length - 3):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = length - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result

def fourSumV3(nums: list[int], target: int) -> list[list[int]]:
    results = []
    if len(nums) < 4:
        return results
    nums.sort()
    n = len(nums)
    for i in range(n-3):
        # remove first duplicate
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i + 1, n - 2):
            # remove second duplicate
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    results.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1  
    return results                              

def run_test_suite():
    # Define test cases. Standardizing nested structures into tuples of sorted tuples
    # lets us accurately verify results regardless of list ordering variants.
    test_cases = [
        {
            "name": "Standard LeetCode Example",
            "nums": [1, 0, -1, 0, -2, 2],
            "target": 0,
            "expected": [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
        },
        {
            "name": "All Elements Identical",
            "nums": [2, 2, 2, 2, 2],
            "target": 8,
            "expected": [[2, 2, 2, 2]],
        },
        {
            "name": "Target Unachievable",
            "nums": [1, 2, 3, 4],
            "target": 100,
            "expected": [],
        },
        {
            "name": "Negative and Zero Target Mix",
            "nums": [-3, -1, 0, 2, 4, 5],
            "target": 2,
            "expected": [
                [-3, -1, 2, 4]
            ],  # One of these matches will fail intentionally below
        },
        # Intentionally adding a failing test case to demonstrate failure counting logic
        # {
        #     "name": "Deliberate Failure Case",
        #     "nums": [0, 0, 0, 0],
        #     "target": 0,
        #     "expected": [[1, 2, 3, 4]]
        # }
    ]

    passed_count = 0
    failed_count = 0

    print("=" * 75)
    print(f"{'RUNNING 4SUM TEST SUITE':^75}")
    print("=" * 75)

    for i, tc in enumerate(test_cases, 1):
        # The implementation is called exactly ONCE per test case here
        # actual = fourSum(tc["nums"], tc["target"])
        # actual = fourSumV2(tc["nums"], tc["target"])
        actual = fourSumV3(tc["nums"], tc["target"])        

        # Format both actual and expected outputs into a standardized set of sorted tuples
        # This completely avoids failing tests due to variant permutations or array configurations.
        actual_set = set(tuple(sorted(q)) for q in actual)
        expected_set = set(tuple(sorted(q)) for q in tc["expected"])

        if actual_set == expected_set:
            passed_count += 1
            status = "✅ PASSED"
            details = f"Found {len(actual)} quadruplet(s)"
        else:
            failed_count += 1
            status = "❌ FAILED"
            details = f"Expected {len(tc['expected'])} matches, got {len(actual)}"

        print(f"Test {i}: {tc['name']:<38} | {status} ({details})")

    print("-" * 75)
    print(f"TOTAL PASSED: {passed_count}")
    print(f"TOTAL FAILED: {failed_count}")
    print(f"SUCCESS RATE: {(passed_count / len(test_cases)) * 100:.1f}%")
    print("=" * 75)


# Run the unified script
if __name__ == "__main__":
    run_test_suite()
