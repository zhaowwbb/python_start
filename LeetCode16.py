import math


def threeSumClosest(nums: list[int], target: int) -> int:
    """
    Finds three integers in nums such that the sum is closest to target.
    Time Complexity: O(N^2) | Space Complexity: O(1) (ignoring sorting allocation)
    """
    nums.sort()
    closest_sum = float("inf")

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                return current_sum

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum


def threeSumClosestV2(nums: list[int], target: int) -> int:
    nums.sort()
    length = len(nums)
    closeSum = -(2**31)
    preDistance = 2**31 - 1
    for i in range(length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        num = nums[i]
        left = i + 1
        right = length - 1
        while left < right:
            total = num + nums[left] + nums[right]
            if total == target:
                return 0
            else:
                distance = abs(total - target)
                if distance < preDistance:
                    closeSum = total
                    preDistance = distance

                if total < target:
                    left += 1
                else:
                    right -= 1

    return closeSum


def threeSumClosestV3(nums: list[int], target: int) -> int:
    nums.sort()
    closeSum = float("inf")
    for i in range(len(nums) - 1):
        # skip duplicate
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return 0
            else:
                if abs(current_sum - target) < abs(closeSum - target):
                    closeSum = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

    return closeSum


def run_test_suite():
    # Define test cases: each dictionary represents one distinct scenario
    test_cases = [
        {
            "name": "Standard LeetCode Example",
            "nums": [-1, 2, 1, -4],
            "target": 1,
            "expected": 2,
        },
        {
            "name": "Exact Match Available",
            "nums": [0, 0, 0],
            "target": 1,
            "expected": 0,
        },
        {
            "name": "All Negative Numbers",
            "nums": [-1, -2, -3, -4],
            "target": -5,
            "expected": -6,
        },
        {
            "name": "Multiple Duplicate Elements",
            "nums": [1, 1, 1, 1],
            "target": 100,
            "expected": 3,
        },
        {
            "name": "Closest Sum is Greater than Target",
            "nums": [1, 2, 3, 4],
            "target": 5,
            "expected": 6,
        },
        {
            "name": "Large Target and Elements",
            "nums": [10, 20, 30, 40, 50],
            "target": 55,
            "expected": 60,
        },
        # Intentionally adding a failing test case to demonstrate failure counting logic
        # {"name": "Deliberate Failure Case", "nums": [1, 1, 1], "target": 3, "expected": 999}
    ]

    passed_count = 0
    failed_count = 0

    print("=" * 60)
    print(f"{'RUNNING 3SUM CLOSEST TEST SUITE':^60}")
    print("=" * 60)

    for i, tc in enumerate(test_cases, 1):
        # The implementation is called exactly ONCE per test case here
        # actual = threeSumClosest(tc["nums"], tc["target"])
        # actual = threeSumClosestV2(tc["nums"], tc["target"])
        actual = threeSumClosestV3(tc["nums"], tc["target"])

        if actual == tc["expected"]:
            passed_count += 1
            status = "✅ PASSED"
            details = f"Result: {actual}"
        else:
            failed_count += 1
            status = "❌ FAILED"
            details = f"Expected {tc['expected']}, got {actual}"

        print(f"Test {i}: {tc['name']:<35} | {status} ({details})")

    print("-" * 60)
    print(f"TOTAL PASSED: {passed_count}")
    print(f"TOTAL FAILED: {failed_count}")
    print(f"SUCCESS RATE: {(passed_count / len(test_cases)) * 100:.1f}%")
    print("=" * 60)


# Run the unified script
if __name__ == "__main__":
    run_test_suite()
