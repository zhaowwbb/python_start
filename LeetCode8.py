# LeetCode 8: String to Integer (atoi)
# Approach: Linear Scan with Boundary Clamping

class Solution:
    def myAtoi(self, s: str) -> int:
        # Define 32-bit signed limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        i = 0
        n = len(s)
        
        # 1. Discard leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
            
        # 2. Check for optional sign indicator
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
            
        # 3. Convert digit characters and handle overflow bounds
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Lookahead overflow check
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
                
            result = result * 10 + digit
            i += 1
            
        return sign * result

    def myAtoiV2(self, s: str) -> int:
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        if len(s) == 0:
            return 0
        i = 0
        sLen = len(s)
        while i < sLen and s[i] == ' ':
            i += 1
        if i == sLen:
            return 0
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            sign = 1
            i += 1
        
        result = 0
        while i < sLen and s[i].isdigit():
            digit = int(s[i])
            if result > MAX_INT // 10 or (result == MAX_INT // 10 and digit > 7):
                if sign > 0:
                    return MAX_INT
                else:
                    return MIN_INT
            
            result = result * 10 + digit
            i += 1
        
        return result * sign                
    
    def myAtoiV3(self, s: str) ->int:
        MIN_INT, MAX_INT = -2**31, 2**31-1
        if len(s) == 0:
            return 0
        n = len(s)
        i = 0
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1 
        elif s[i] == '+':
            i += 1
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if result > MAX_INT // 10 or (result == MAX_INT // 10 and digit > 7):
                return MAX_INT if sign > 0 else MIN_INT
            
            result = result * 10 + digit
            i += 1
            
        return result * sign               
    
# --- Test Logic ---
def run_tests():
    solution = Solution()
    
    test_cases = [
        {"input": "42", "expected": 42, "desc": "Standard positive integer conversion"},
        {"input": "   -42", "expected": -42, "desc": "Leading spaces and negative sign conversion"},
        {"input": "1337c0d3", "expected": 1337, "desc": "Conversion stops at first non-digit letter"},
        {"input": "0-1", "expected": 0, "desc": "Conversion stops due to internal non-digit symbols"},
        {"input": "words and 987", "expected": 0, "desc": "Starts with words, should return 0"},
        {"input": "-91283472332", "expected": -2147483648, "desc": "Underflow clamping limit test"}
    ]
    
    print("Running LeetCode 8 - String to Integer (atoi) Tests:\n" + "="*50)
    passed = 0
    
    for i, tc in enumerate(test_cases, 1):
        # result = solution.myAtoi(tc["input"])
        # result = solution.myAtoiV2(tc["input"])    
        result = solution.myAtoiV3(tc["input"])         
            
        status = "PASSED" if result == tc["expected"] else "FAILED"
        
        if status == "PASSED":
            passed += 1
            
        print(f"Test {i}: {tc['desc']}")
        print(f"  Input:    '{tc['input']}'")
        print(f"  Result:   {result}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Status:   {status}\n")
        
    print("="*50)
    print(f"Summary: {passed}/{len(test_cases)} tests passed.")

if __name__ == "__main__":
    run_tests()