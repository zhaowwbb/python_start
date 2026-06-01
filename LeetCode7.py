# LeetCode 7: Reverse Integer
# Approach: Extracting Digits and Simulating 32-bit Integer Overflow

class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        reversed_num = 0
        # Determine the sign of the integer
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            # Extract the last digit
            pop = x % 10
            x //= 10
            
            # Python supports arbitrarily large integers. To strictly simulate 
            # 32-bit environment constraints, we check bounds manually before updating.
            if sign == 1:
                if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and pop > 7):
                    return 0
            else:
                # For negative numbers, absolute threshold mirrors differently 
                # (INT_MIN ends in -8, absolute value threshold ends in 8)
                if reversed_num > abs(INT_MIN) // 10 or (reversed_num == abs(INT_MIN) // 10 and pop > 8):
                    return 0
                    
            reversed_num = reversed_num * 10 + pop
            
        return sign * reversed_num

    def reverseV2(self, x: int) ->int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        rev = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x != 0:
            pop = x % 10
            x //= 10
            if sign == 1:                
                if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop >7):
                    return 0
            else:
                if rev > abs(INT_MIN) // 10 or (rev == abs(INT_MIN) // 10 and pop> 8):
                    return 0 
            rev = rev * 10 + pop    

        return rev * sign
    
    def reverseV3(self, x : int) ->int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        rev = 0
        
        sign = 1 if x > 0 else -1
        x = abs(x)
        # print("V3 sign=", sign)
        
        while x != 0:
            pop = x % 10
            x //= 10
            if sign:
                if rev > INT_MAX//10 or (rev == INT_MAX//10 and pop > 7):
                    return 0
            else:
                if rev > abs(INT_MIN)//10 or (rev == abs(INT_MIN)//10 and pop >8):
                    return 0
            rev = rev * 10 + pop
        
        return rev * sign    
    
    def reverseV4(self, x: int) ->int:
        INT_MAX = 2**31 -1
        INT_MIN = -2**31
        rev = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x != 0 :
            pop = x % 10
            x //= 10
            if sign:
                if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
                    return 0
            else:
                if rev > abs(INT_MIN)//10 or (rev == abs(INT_MIN) //10 and pop > 8):
                    return 0
            rev = rev * 10 + pop  
        
        return rev * sign          

                
# --- Test Logic ---
def run_tests():
    solution = Solution()
    
    test_cases = [
        {"input": 123, "expected": 321, "desc": "Standard positive integer"},
        {"input": -123, "expected": -321, "desc": "Standard negative integer"},
        {"input": 120, "expected": 21, "desc": "Integer ending with zero"},
        {"input": 0, "expected": 0, "desc": "Zero check"},
        {"input": 1534236469, "expected": 0, "desc": "Overflow scenario (exceeds 32-bit INT_MAX upon reversal)"},
        {"input": -2147483648, "expected": 0, "desc": "Underflow limit check"}
    ]
    
    print("Running LeetCode 7 - Reverse Integer Tests:\n" + "="*50)
    passed = 0
    
    for i, tc in enumerate(test_cases, 1):
        # result = solution.reverse(tc["input"])
        # result = solution.reverseV2(tc["input"])  
        # result = solution.reverseV3(tc["input"])    
        result = solution.reverseV4(tc["input"])                     
        status = "PASSED" if result == tc["expected"] else "FAILED"
        
        if status == "PASSED":
            passed += 1
            
        print(f"Test {i}: {tc['desc']}")
        print(f"  Input:    {tc['input']}")
        print(f"  Result:   {result}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Status:   {status}\n")
        
    print("="*50)
    print(f"Summary: {passed}/{len(test_cases)} tests passed.")

if __name__ == "__main__":
    run_tests()