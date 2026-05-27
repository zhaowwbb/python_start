# LeetCode33.py
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
            
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
                
            # Check if the left half is normally sorted
            if nums[left] <= nums[mid]:
                # Check if target lies within the sorted left half range
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left
                else:
                    left = mid + 1   # Search right
            # Otherwise, the right half must be normally sorted
            else:
                # Check if target lies within the sorted right half range
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Search right
                else:
                    right = mid - 1  # Search left
                    
        return -1

    def searchV2(self, nums : List[int], target : int) ->int:
        if not nums:
            return -1
        left, right = 0, len(nums) -1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1                                
    
    def searchV3(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1    
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1                
                    

if __name__ == "__main__":
    solution = Solution()
    
    # Define test cases: (nums, target, expected_output, description)
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4, "Example 1: Target exists in the right rotated part"),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1, "Example 2: Target does not exist"),
        ([1], 0, -1, "Example 3: Single element array, target does not exist"),
        ([1], 1, 0, "Single element array, target exists"),
        ([5, 1, 3], 3, 2, "Small rotated array, target on the right"),
        ([3, 5, 1], 3, 0, "Small rotated array, target on the left")
    ]
    
    print("Running LeetCode 33 - Search in Rotated Sorted Array Tests:\n" + "="*60)
    
    all_passed = True
    for i, (nums, target, expected, desc) in enumerate(test_cases, 1):
        # Each test case explicitly invokes the search function exactly once
        # result = solution.search(nums, target)
        # result = solution.searchV2(nums, target)
        result = solution.searchV3(nums, target)
        
        status = "PASSED" if result == expected else "FAILED"
        if result != expected:
            all_passed = False
            
        print(f"Test {i}: {desc}")
        print(f"  Input: nums = {nums}, target = {target}")
        print(f"  Expected: {expected}, Got: {result}")
        print(f"  Status: {status}\n")
        
    print("="*60)
    if all_passed:
        print("All test cases PASSED successfully!")
    else:
        print("Some test cases FAILED.")