class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # '//' handles integer division in Python
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                left = mid + 1  # Target is in the right half
            else:
                right = mid - 1  # Target is in the left half

        # If not found, 'left' holds the correct insertion index
        return left

    def searchInsertV2(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) -1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left            
                    

# --- Test Logic ---
if __name__ == "__main__":
    solution = Solution()

    # List of test cases: (nums, target, expected_result)
    test_cases = [
        ([1, 3, 5, 6], 5, 2),  # Example 1: Target exists
        ([1, 3, 5, 6], 2, 1),  # Example 2: Target missing, falls in middle
        ([1, 3, 5, 6], 7, 4),  # Example 3: Target missing, falls at the end
        ([1, 3, 5, 6], 0, 0),  # Example 4: Target missing, falls at the start
        ([1], 1, 0),           # Example 5: Single element array, target exists
        ([1], 0, 0),           # Example 6: Single element array, target missing
    ]

    print("=" * 60)
    print(f"{'INPUT':<25} | {'EXPECTED':<10} | {'ACTUAL':<10} | {'STATUS'}")
    print("=" * 60)

    for i, (nums, target, expected) in enumerate(test_cases, 1):
        # actual = solution.searchInsert(nums, target)
        actual = solution.searchInsertV2(nums, target)
        status = "✅ PASS" if actual == expected else "❌ FAIL"
        
        # Format the input string nicely for the display table
        input_str = f"nums={nums}, t={target}"
        print(f"{input_str:<25} | {expected:<10} | {actual:<10} | {status}")

    print("=" * 60)