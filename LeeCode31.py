def nextPermutation(nums):
    print("start testing")
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
        
    if i == -1 :
        nums.reverse()
        return
    
    j = len(nums) - 1
    while nums[i] >= nums[j]:
        j -= 1
        
    nums[i], nums[j] = nums[j], nums[i]   
    
    nums[i + 1:] = reversed(nums[i + 1:]) 
       
def nextPermutationV2(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
        
    if i == -1:
        nums.reverse()
        return
    
    j = len(nums) - 1
    while nums[i] >= nums[j]:
        j -= 1
        
    nums[i], nums[j] = nums[j], nums[i]
    
    nums[i + 1:] = reversed(nums[i+1:])        
    
if __name__ == "__main__":
    # tests = [
    test_cases = [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1, 3, 2], [2, 1, 3]),
        ([2, 3, 1], [3, 1, 2]),
        ([5, 4, 7, 5, 3, 2], [5,5,2,3,4,7]),
        ([4, 2, 0, 2, 3, 2, 0], [4,2,0,3,0,2,2]),                
    ]

    for original, expected in test_cases:
        nums = original[:]  # copy for processing
        # nextPermutation(nums)
        nextPermutationV2(nums)
        print(f"Input: {original} | Expected: {expected} | Actual: {nums}")   