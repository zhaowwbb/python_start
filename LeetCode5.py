# LeetCode 5: Longest Palindromic Substring
# Approach: Expand Around Center

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            # Case 1: Odd length palindrome (centered at i)
            len1 = self._expand_around_center(s, i, i)
            # Case 2: Even length palindrome (centered between i and i+1)
            len2 = self._expand_around_center(s, i, i + 1)
            
            # Find the maximum length from both cases
            max_len = max(len1, len2)
            
            # If a longer palindrome is found, update start and end bounds
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]

    def _expand_around_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Length of the palindrome is right - left - 1
        return right - left - 1

    def longestPalindromeV2(self, s: str) -> str:
        left, right, maxLen = 0, 0, 0
        # maxLen = 0
        
        for i in range(len(s)):
            len1 = self.expandFromCenterV2(s, i, i)
            len2 = self.expandFromCenterV2(s, i, i + 1)
            maxLen = max(len1, len2)
            if maxLen > right - left + 1:
                left = i - (maxLen - 1)//2
                right = i + (maxLen//2)
        
        return s[left:right + 1]
    
    def expandFromCenterV2(self, s: str, left: int, right: int) -> int:
        while left >=0 and right < len(s) and s[left] == s[right]:
            left-= 1
            right+= 1
        return right - left - 1    

    def longestPalindromeV3(self, s: str) -> str:
        left, right, maxLen = 0, 0, 0
        for i in range(len(s)):
            len1 = self.expandFromCenterV3(s, i, i)
            len2 = self.expandFromCenterV3(s, i, i+1)
            maxLen = max(len1, len2)
            if maxLen > right - left + 1:
                left = i - (maxLen - 1)//2
                right = i + maxLen//2
        
        return s[left: right + 1]        
    
    def expandFromCenterV3(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return right - left - 1
               

# --- Test Logic ---
def run_tests():
    solution = Solution()
    
    test_cases = [
        {"input": "babad", "expected": ["bab", "aba"], "desc": "Standard odd/even palindromes mixed"},
        {"input": "cbbd", "expected": ["bb"], "desc": "Even-length palindrome"},
        {"input": "a", "expected": ["a"], "desc": "Single character"},
        {"input": "ac", "expected": ["a", "c"], "desc": "Two distinct characters"},
        {"input": "racecar", "expected": ["racecar"], "desc": "Full string is a palindrome"},
        {"input": "aacabdkacaa", "expected": ["aca"], "desc": "Longer string with internal palindrome"}
    ]
    
    print("Running LeetCode 5 - Longest Palindromic Substring Tests:\n" + "="*50)
    passed = 0
    
    for i, tc in enumerate(test_cases, 1):
        # result = solution.longestPalindrome(tc["input"])
        # result = solution.longestPalindromeV2(tc["input"])
        result = solution.longestPalindromeV3(tc["input"])        
        
        # Check if result matches any of the valid expected answers
        status = "PASSED" if result in tc["expected"] else "FAILED"
        
        if status == "PASSED":
            passed += 1
            
        print(f"Test {i}: {tc['desc']}")
        print(f"  Input:    '{tc['input']}'")
        print(f"  Result:   '{result}'")
        print(f"  Expected: {tc['expected']}")
        print(f"  Status:   {status}\n")
        
    print("="*50)
    print(f"Summary: {passed}/{len(test_cases)} tests passed.")

if __name__ == "__main__":
    run_tests()