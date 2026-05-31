# LeetCode 3: Longest Substring Without Repeating Characters
# Language: Python 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters
        using an optimized sliding window approach with a hash map.
        
        Time Complexity: O(n) - Single pass through the string
        Space Complexity: O(min(m, n)) - Space for the hash map tracking character indices
        """
        char_map = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            current_char = s[right]
            
            # If the character is a duplicate and falls within our current window
            if current_char in char_map:
                # Move the left pointer past the duplicate's last seen position
                left = max(left, char_map[current_char] + 1)
            
            # Record/update the index of the current character
            char_map[current_char] = right
            
            # Update the maximum length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length

    def lengthOfLongestSubstringV2(self, s: str) -> int:
        if not s:
            return 0
        charToIndex = {}
        left = 0
        maxLen = 0
        for right, c in enumerate(s):
            # c = s[right]
            if c in charToIndex:
                left = max(left, charToIndex[c] + 1)
            charToIndex[c] = right
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen        

    def lengthOfLongestSubstringV3(self, s: str) -> int:
        if not s:
            return 0
        charToIndex = {}
        maxLen = 0
        left = 0
        for right in range(len(s)):
            c = s[right]
            if c in charToIndex:
                left = max(left, charToIndex[c] + 1)
            charToIndex[c] = right
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen    

# ==========================================
# TEST LOGIC
# ==========================================
def run_tests():
    solver = Solution()
    
    test_cases = [
        {"input": "abcabcbb", "expected": 3, "desc": "Standard mixed repeating characters"},
        {"input": "bbbbb", "expected": 1, "desc": "All identical characters"},
        {"input": "pwwkew", "expected": 3, "desc": "Substring inside a subsequence pattern"},
        {"input": "", "expected": 0, "desc": "Empty string boundary case"},
        {"input": " ", "expected": 1, "desc": "Single space string"},
        {"input": "au", "expected": 2, "desc": "Two distinct characters"},
        {"input": "dvdf", "expected": 3, "desc": "Repeated character separated by others"},
        {"input": "abcdefghijklmnopqrstuvwxyz", "expected": 26, "desc": "All unique characters"},
        {"input": "1234!@#$ 1234", "expected": 9, "desc": "Includes digits, symbols, and spaces"}
    ]
    
    print("=" * 60)
    print("RUNNING UNIT TESTS FOR LEETCODE 3")
    print("=" * 60)
    
    passed_count = 0
    
    for i, test in enumerate(test_cases, 1):
        # actual = solver.lengthOfLongestSubstring(test["input"])
        # actual = solver.lengthOfLongestSubstringV2(test["input"])  
        actual = solver.lengthOfLongestSubstringV3(test["input"])              
        status = "PASSED ✅" if actual == test["expected"] else "FAILED ❌"
        
        if actual == test["expected"]:
            passed_count += 1
            
        print(f"Test {i}: {test['desc']}")
        print(f"  Input:    {repr(test['input'])}")
        print(f"  Expected: {test['expected']}")
        print(f"  Actual:   {actual}")
        print(f"  Status:   {status}")
        print("-" * 40)
        
    print(f"Final Summary: {passed_count}/{len(test_cases)} tests passed.")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()