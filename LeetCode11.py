class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the width between the two vertical lines
            width = right - left
            
            # The height of the water is bounded by the shorter line
            current_height = min(height[left], height[right])
            
            # Calculate current area and update max_water if it's larger
            current_area = width * current_height
            if current_area > max_water:
                max_water = current_area
                
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water

    def maxAreaV2(self, height: list[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height
            if area > max_area:
                max_area = area
            if  height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area      

# --- Test Logic Framework ---

class TestCase:
    def __init__(self, height: list[int], expected: int):
        self.height = height
        self.expected = expected


if __name__ == "__main__":
    solver = Solution()

    # Defining multiple test cases
    test_cases = [
        TestCase(
            height=[1, 8, 6, 2, 5, 4, 8, 3, 7],
            expected=49
        ),
        TestCase(
            height=[1, 1],
            expected=1
        ),
        TestCase(
            height=[4, 3, 2, 1, 4],
            expected=16
        ),
        TestCase(
            height=[1, 2, 1],
            expected=2
        )
    ]

    print("Executing Container With Most Water Automation Suite...\n")
    passed_count = 0

    for idx, tc in enumerate(test_cases, 1):
        # Call the implementation method ONLY ONE time per test case execution
        # actual_result = solver.maxArea(tc.height)
        actual_result = solver.maxAreaV2(tc.height)
        
        is_passed = actual_result == tc.expected
        if is_passed:
            passed_count += 1

        status = "✅ PASS" if is_passed else "❌ FAIL"
        print(f"Test Case {idx}: {status}")
        print(f"  Heights : {tc.height}")
        print(f"  Expected: {tc.expected}")
        print(f"  Actual  : {actual_result}")
        print("-" * 67)

    print(f"Test Run Complete: {passed_count}/{len(test_cases)} Passed.")