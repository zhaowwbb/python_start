def isMatch(s: str, p: str) -> bool:
    if s is None or p is None:
        return False

    m, n = len(s), len(p)

    # dp[i][j] will be True if s[0..i-1] matches p[0..j-1]
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: empty string matches empty pattern
    dp[0][0] = True

    # Deals with patterns like a*, a*b*, a*b*c* matching an empty string s
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            current_p = p[j - 1]
            current_s = s[i - 1]

            if current_p == current_s or current_p == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif current_p == '*':
                # Case 1: Count '*' as 0 occurrences of the preceding element
                dp[i][j] = dp[i][j - 2]

                # Case 2: Count '*' as 1 or more occurrences
                # This is only valid if the preceding character in p matches current_s
                predecessor_p = p[j - 2]
                if predecessor_p == current_s or predecessor_p == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[m][n]

def isMatchV2(s: str, p: str) ->bool:
    m,n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(1, n+ 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j -2]
            
    for i in range(1, m+1):
        for j in range(1, n+1):
            curS = s[i -1]
            curP = p[j -1]
            if curS == curP or curP == '.':
                dp[i][j] = dp[i-1][j-1]
            elif curP == '*':
                dp[i][j] = dp[i][j-2]
                preP = p[j-2]
                if preP == curS or preP == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]
    return dp[m][n]                            

def isMatchV3(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n+1) for _ in range(m+1)]
    dp[0][0] = True
    for j in range(1, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            curS = s[i-1]
            curP = p[j-1]
            if curS == curP or curP == '.':
                dp[i][j] = dp[i-1][j-1]
            elif curP == '*':
                dp[i][j] = dp[i][j-2]
                
                preP = p[j-2]
                if curS == preP or preP == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]    
    
    return dp[m][n]        
            

def run_tests():
    # Structured array containing test cases with explicit metadata
    test_cases = [
        {"s": "aa", "p": "a", "expected": False, "desc": "Exact character mismatch (length difference)"},
        {"s": "aa", "p": "a*", "expected": True, "desc": "Star operator (*) matching multiple characters"},
        {"s": "ab", "p": ".*", "expected": True, "desc": "Dot-Star (.*) matching any sequence"},
        {"s": "aab", "p": "c*a*b", "expected": True, "desc": "Preceding element with 0-occurrence star matching"},
        {"s": "mississippi", "p": "mis*is*p*.", "expected": False, "desc": "Complex combination resulting in mismatch"},
        {"s": "ab", "p": ".*c", "expected": False, "desc": "Dot-Star match fails due to trailing character requirement"}
    ]
    
    print("Running LeetCode 10 - Regular Expression Matching Tests:\n" + "="*65)
    passed = 0
    
    for i, tc in enumerate(test_cases, 1):
        # Call the function exactly ONE time per test case
        # result = isMatch(tc["s"], tc["p"])
        # result = isMatchV2(tc["s"], tc["p"])        
        result = isMatchV3(tc["s"], tc["p"]) 
        
        print(f"Test {i}: {tc['desc']}")
        print(f"  Input String  (s): {tc['s']}")
        print(f"  Input Pattern (p): {tc['p']}")
        print(f"  Expected Result:   {tc['expected']}")
        print(f"  Actual Result:     {result}")
        
        if result == tc["expected"]:
            print("  Status:            PASSED ✅")
            passed += 1
        else:
            print("  Status:            FAILED ❌")
        print("-" * 45)
        
    print(f"\nResult: {passed}/{len(test_cases)} tests passed.")


if __name__ == '__main__':
    run_tests()