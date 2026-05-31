# LeetCode 4: Median of Two Sorted Arrays
# Language: Python 3
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted arrays using binary search on partitions.
        
        Time Complexity: O(log(min(m, n))) - Satisfies the O(log(m+n)) requirement.
        Space Complexity: O(1) - Constant auxiliary space.
        """
        # Ensure nums1 is the shorter array to optimize the binary search range
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left = (m + n + 1) // 2
        
        while low <= high:
            # Partition indices
            i = (low + high) // 2
            j = total_left - i
            
            # Boundary values around the partition cuts (handle edges using infinity)
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            # Check if partition is valid
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Odd combined length
                if (m + n) % 2 != 0:
                    return float(max(nums1_left_max, nums2_left_max))
                # Even combined length
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
            
            # Too far right in nums1, move partition left
            elif nums1_left_max > nums2_right_min:
                high = i - 1
            # Too far left in nums1, move partition right
            else:
                low = i + 1
                
        raise ValueError("Input arrays are not properly sorted.")

    def findMedianSortedArraysV2(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArraysV2(nums2, nums1)
        m, n = len(nums1), len(nums2)
        totalLeft = (m + n + 1)//2
        left, right = 0, m
        while left <= right:
            p1 = (left + right) // 2
            p2 = totalLeft - p1
            
            leftMax1 = float('-inf') if p1 == 0 else nums1[p1 -1]
            rightMin1 = float('inf') if p1 == m else nums1[p1]
            leftMax2 = float('-inf') if p2 == 0 else nums2[p2 - 1]
            rightMin2 = float('inf') if p2 == n else nums2[p2]
            
            if leftMax1 <= rightMin2 and leftMax2 <= rightMin1:
                if (m + n)% 2 != 0:
                    return float(max(leftMax1, leftMax2))
                else:
                    return (max(leftMax1, leftMax2) + min(rightMin1, rightMin2))/2.0
            elif leftMax1 > rightMin2:
                right = p1 -1
            else:
                left = p1 + 1                        
        
        raise ValueError("Array not properly sorted")

    def findMedianSortedArraysV3(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArraysV3(nums2, nums1)
        
        m , n = len(nums1), len(nums2)
        left, right = 0, m
        halfSize = (m + n + 1) // 2
        
        while left <= right:
            p1 = (left + right) // 2
            p2 = halfSize - p1
            
            leftMax1 = float('-inf') if p1 == 0 else nums1[p1 - 1]
            rightMin1 = float('inf') if p1 == m else nums1[p1]
            leftMax2 = float('-inf') if p2 == 0 else nums2[p2 - 1]
            rightMin2 = float('inf') if p2 == n else nums2[p2]
            
            if leftMax1 <= rightMin2 and leftMax2 <= rightMin1:
                if (m + n) % 2 != 0:
                    return float(max(leftMax1, leftMax2))
                else:
                    return (max(leftMax1, leftMax2) + min(rightMin1, rightMin2)) / 2.0
            elif leftMax1 > rightMin2:
                right = p1 -1
            else:
                left = p1 + 1
                
        raise ValueError("Input array not sorted")                

# ==========================================
# TEST LOGIC
# ==========================================
def run_tests():
    solver = Solution()
    
    test_cases = [
        {
            "nums1": [1, 3], "nums2": [2], 
            "expected": 2.0, "desc": "Example 1: Odd combined total"
        },
        {
            "nums1": [1, 2], "nums2": [3, 4], 
            "expected": 2.5, "desc": "Example 2: Even combined total"
        },
        {
            "nums1": [], "nums2": [1], 
            "expected": 1.0, "desc": "First array is empty"
        },
        {
            "nums1": [3], "nums2": [], 
            "expected": 3.0, "desc": "Second array is empty"
        },
        {
            "nums1": [1, 2], "nums2": [1, 2, 3], 
            "expected": 2.0, "desc": "Overlapping arrays"
        },
        {
            "nums1": [-5, 3, 6, 12, 15], "nums2": [-12, -2, 0, 11, 20], 
            "expected": 4.5, "desc": "Includes negative numbers"
        },
        {
            "nums1": [1, 2, 3], "nums2": [4, 5, 6, 7, 8], 
            "expected": 4.5, "desc": "Completely disjoint sets"
        }
    ]
    
    print("=" * 65)
    print("RUNNING UNIT TESTS FOR LEETCODE 4 (MEDIAN OF SORTED ARRAYS)")
    print("=" * 65)
    
    passed_count = 0
    
    for i, test in enumerate(test_cases, 1):
        # actual = solver.findMedianSortedArrays(test["nums1"], test["nums2"])
        # actual = solver.findMedianSortedArraysV2(test["nums1"], test["nums2"])        
        actual = solver.findMedianSortedArraysV3(test["nums1"], test["nums2"])           
        status = "PASSED ✅" if actual == test["expected"] else "FAILED ❌"
        
        if actual == test["expected"]:
            passed_count += 1
            
        print(f"Test {i}: {test['desc']}")
        print(f"  Array 1:  {test['nums1']}")
        print(f"  Array 2:  {test['nums2']}")
        print(f"  Expected: {test['expected']} | Actual: {actual}")
        print(f"  Status:   {status}")
        print("-" * 45)
        
    print(f"Final Summary: {passed_count}/{len(test_cases)} tests passed.")
    print("=" * 65)

if __name__ == "__main__":
    run_tests()