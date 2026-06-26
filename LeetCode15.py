class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []
        length = len(nums)
        
        for i in range(length - 2):
            # If the current number is > 0, the remaining numbers will also be > 0.
            # No three positive numbers can sum to 0.
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = length - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
        return results

    def threeSumV2(self, nums : list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return []
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            num = nums[i]
            if num > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+ 1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1 
                    right -= 1                       
                elif total > 0:
                    right -= 1
                else:
                    left += 1                        
        
        return result
    
    def threeSumV3(self, nums: list[int]) -> list[list[int]]:
        results = []
        if len(nums) == 0:
            return results
        nums.sort()
        length = len(nums)
        
        for i in range(length - 2):
            num = nums[i]
            # invalid data
            if num > 0:
                break
            
            # remove duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = length - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])  
                    while left < right and nums[left] == nums[left+ 1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results                 

def run_tests():
    solution = Solution()
    
    # Define test cases: (input_data, expected_output)
    # Note: Order of triplets or numbers inside triplets doesn't matter for correctness,
    # but since our code sorts them, the expected values are also sorted for easy assertion.
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]), # Case 1: Standard LeetCode example
        ([0, 1, 1], []),                                    # Case 2: No valid triplet
        ([0, 0, 0], [[0, 0, 0]]),                           # Case 3: All zeros
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),                   # Case 4: Handling duplicate triplets
        ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 4], [           # Case 5: Complex array with multiple matches
            [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], 
            [-2, -2, 4], [-2, 0, 2]
        ]),
        ([], []),                                           # Case 6: Empty array
        ([1, 2], [])                                        # Case 7: Fewer than 3 elements
    ]
    
    passed_count = 0
    failed_count = 0
    
    print("--- Running LeetCode 15 Tests (3Sum) ---")
    
    for index, (inputs, expected) in enumerate(test_cases, start=1):
        # Implementation is called exactly once per test case
        # result = solution.threeSum(inputs)
        # result = solution.threeSumV2(inputs)        
        result = solution.threeSumV3(inputs)  
        
        # Helper check to ensure order-agnostic matching of the inner contents
        # (Converting to sorted lists/tuples ensures match correctness regardless of engine output array order)
        sorted_result = sorted([sorted(triplet) for triplet in result])
        sorted_expected = sorted([sorted(triplet) for triplet in expected])
        
        if sorted_result == sorted_expected:
            print(f"Test Case {index}: PASSED")
            passed_count += 1
        else:
            print(f"Test Case {index}: FAILED")
            print(f"   Expected: {expected}")
            print(f"   Got:      {result}")
            failed_count += 1
            
    print("----------------------------------------")
    print(f"Summary: {passed_count} passed, {failed_count} failed.")


if __name__ == "__main__":
    run_tests()