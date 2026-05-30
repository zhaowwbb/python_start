# LeetCode1.py

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the number as the key and its index as the value
        num_to_index = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            complement = target - num
            
            # If the complement exists in our dictionary, we found the pair
            if complement in num_to_index:
                return [num_to_index[complement], i]
                
            # Otherwise, store the current number and its index
            num_to_index[num] = i
            
        # Return empty list if no solution is found (though constraints guarantee one exists)
        return []

    def twoSumV2(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return[]    

    def twoSumV3(self, nums: List[int], target: int) ->List[int]:
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []

# --- Main Function with Looped Test Cases ---
if __name__ == "__main__":
    solution = Solution()
    
    # Test case group containing all scenario data
    test_cases = [
        {
            "id": 1,
            "nums": [2, 7, 11, 15],
            "target": 9,
            "expected": [0, 1]
        },
        {
            "id": 2,
            "nums": [3, 2, 4],
            "target": 6,
            "expected": [1, 2]
        },
        {
            "id": 3,
            "nums": [3, 3],
            "target": 6,
            "expected": [0, 1]
        }
    ]
    
    # Loop through the test case group
    for tc in test_cases:
        # Call implementation function exactly once
        # actual_result = solution.twoSum(tc["nums"], tc["target"])
        # actual_result = solution.twoSumV2(tc["nums"], tc["target"])
        actual_result = solution.twoSumV3(tc["nums"], tc["target"])
        
        print(f"Test Case {tc['id']}:")
        print(f"  nums:     {tc['nums']}")
        print(f"  target:   {tc['target']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Actual:   {actual_result}")
        print("-" * 40)