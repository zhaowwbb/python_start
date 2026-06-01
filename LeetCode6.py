# LeetCode 6: Zigzag Conversion
# Approach: Simulating Row-by-Row Traversal using Character Buckets

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Base Case: If there's only 1 row or the rows exceed string length,
        # the zigzag layout remains identical to the original sequence.
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize a bucket/string for each row
        rows = [""] * numRows
        curr_row = 0
        going_down = False
        
        # Distribute characters into their corresponding row bucket
        for char in s:
            rows[curr_row] += char
            
            # Switch direction whenever we reach the top (0) or bottom (numRows - 1)
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
                
            # Move index up or down depending on the direction
            curr_row += 1 if going_down else -1
            
        # Join all the rows sequentially to form the final result
        return "".join(rows)

    def convertV2(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        currentRow = 0
        goDown = False
        rows = [""]*numRows
        for c in s:
            rows[currentRow] += c
            if currentRow == 0 or currentRow == numRows - 1:
                goDown = not goDown
                
            if goDown:
                currentRow += 1
            else:
                currentRow -= 1
                
        return "".join(rows)                

    def convertV3(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        
        goDown = False
        currentRow = 0
        rows = [""]*numRows
        for c in s:
            rows[currentRow] += c
            if currentRow == 0 or currentRow == numRows - 1:
                goDown = not goDown
            
            currentRow += 1 if goDown else -1
            
        return "".join(rows)
                

# --- Test Logic ---
def run_tests():
    solution = Solution()
    
    test_cases = [
        {"s": "PAYPALISHIRING", "numRows": 3, "expected": "PAHNAPLSIIGYIR", "desc": "Standard zigzag with 3 rows"},
        {"s": "PAYPALISHIRING", "numRows": 4, "expected": "PINALSIGYAHRPI", "desc": "Standard zigzag with 4 rows"},
        {"s": "A", "numRows": 1, "expected": "A", "desc": "Single character string"},
        {"s": "AB", "numRows": 1, "expected": "AB", "desc": "Multiple characters with single row"},
        {"s": "ABCD", "numRows": 5, "expected": "ABCD", "desc": "numRows greater than string length"}
    ]
    
    print("Running LeetCode 6 - Zigzag Conversion Tests:\n" + "="*50)
    passed = 0
    
    for i, tc in enumerate(test_cases, 1):
        # result = solution.convert(tc["s"], tc["numRows"])
        # result = solution.convertV2(tc["s"], tc["numRows"])
        result = solution.convertV3(tc["s"], tc["numRows"])                    
        status = "PASSED" if result == tc["expected"] else "FAILED"
        
        if status == "PASSED":
            passed += 1
            
        print(f"Test {i}: {tc['desc']}")
        print(f"  Input String: '{tc['s']}' | numRows: {tc['numRows']}")
        print(f"  Result:       '{result}'")
        print(f"  Expected:     '{tc['expected']}'")
        print(f"  Status:       {status}\n")
        
    print("="*50)
    print(f"Summary: {passed}/{len(test_cases)} tests passed.")

if __name__ == "__main__":
    run_tests()