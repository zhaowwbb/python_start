# LeetCode34.py
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
            
        def findBound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        right = mid - 1  # Narrow down to look for smaller indices on the left
                    else:
                        left = mid + 1   # Narrow down to look for larger indices on the right
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return bound
            
        first_pos = findBound(is_first=True)
        if first_pos == -1:
            return [-1, -1]
            
        last_pos = findBound(is_first=False)
        return [first_pos, last_pos]

    def searchRangeV2(self, nums: List[int], target: int) ->List[int]:
        if not nums:
            return [-1, -1]
        
        def findBoundV2(is_first : bool) ->int:            
            left, right = 0, len(nums) - 1  
            bound = -1      
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1                
            return bound
        
        first_pos = findBoundV2(is_first=True)
        if first_pos == -1:
            return [-1, -1]
        
        second_pos = findBoundV2(is_first=False)
        return [first_pos, second_pos]    
    
    def searchRangeV3(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        def findBoundV3(is_first : bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return bound
        
        first_pos = findBoundV3(is_first=True)
        if first_pos == -1:
            return [-1, -1]
        
        second_pos = findBoundV3(is_first=False)
        return [first_pos, second_pos]                    
                    

if __name__ == "__main__":
    solution = Solution()
    
    # Define test cases: (nums, target, expected_output, description)
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4], "Example 1: Target exists multiple times"),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1], "Example 2: Target does not exist inside array bounds"),
        ([], 0, [-1, -1], "Example 3: Empty array"),
        ([2, 2], 2, [0, 1], "All elements match the target"),
        ([1, 2, 3, 4, 5], 3, [2, 2], "Target appears exactly once in the middle"),
        ([1, 3, 5, 7, 9], 10, [-1, -1], "Target is greater than all elements")
    ]
    
    print("Running LeetCode 34 - Find First and Last Position Tests:\n" + "="*60)
    
    all_passed = True
    for i, (nums, target, expected, desc) in enumerate(test_cases, 1):
        # Each test case explicitly executes the searchRange function exactly once
        # result = solution.searchRange(nums, target)
        # result = solution.searchRangeV2(nums, target)
        result = solution.searchRangeV3(nums, target)
        
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