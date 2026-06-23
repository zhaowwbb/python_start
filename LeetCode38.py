import time
from typing import List, Optional

class LeetCode38:
    # Class-level cache array initialized to match the 1 <= n <= 30 constraints.
    # index 0 is unused; indices 1 to 30 will hold the strings.
    _memo: List[Optional[str]] = [None] * 31

    def countAndSay(self, n: int) -> str:
        # Base case initialization
        if self._memo[1] is None:
            self._memo[1] = "1"
        
        # Fill the cache up to n if not already computed
        for i in range(2, n + 1):
            if self._memo[i] is None:
                self._memo[i] = self._getNextSequence(self._memo[i - 1])
                
        return self._memo[n]

    def _getNextSequence(self, s: str) -> str:
        res = []
        i, length = 0, len(s)
        
        while i < length:
            current_char = s[i]
            count = 0
            
            # Count consecutive identical characters
            while i < length and s[i] == current_char:
                count += 1
                i += 1
                
            # Append frequency followed by the character itself
            res.append(str(count))
            res.append(current_char)
            
        return "".join(res)
    
    def countAndSayV2(self, n : int) -> str:
        if n == 1:
            return "1"
        input = "1"
        output = ""
        for i in range (2, n+1):
            output= self.getNextSequenceV2(input)
            input = output
            
        return output
        
    def getNextSequenceV2(self, s : str) -> str:
        i, length = 0, len(s)
        output = []
        while i < length:
            current = s[i]
            count = 0
            while i < length and s[i] == current:
                count+=1
                i+=1
            output.append(str(count))
            output.append(current)   
        
        return "".join(output)             
    
    def countAndSayV3(self, n: int) -> str:
        if self._memo[1] == None:
            self._memo[1] = "1"
        if n == 1:
            return self._memo[1]
        
        for i in range(2, n + 1):
            input = self._memo[i - 1]
            self._memo[i] = self._getNextSequenceV3(input)
            
        return self._memo[n]    
        
    def _getNextSequenceV3(self, s : str) -> str:
        output = []
        i, length = 0, len(s)
        while i < length:
            current = s[i]
            count = 0
            while i < length and s[i] ==  current:
                count += 1
                i += 1
            output.append(str(count))
            output.append(current)    
        
        return "".join(output)
                   

if __name__ == "__main__":
    solver = LeetCode38()

    # Multi-case datasets
    testInputs = [1, 2, 3, 4, 5]
    expectedOutputs = ["1", "11", "21", "1211", "111221"]

    print("--- Running Count and Say Tests ---")

    # Single function call execution within the loop
    for i in range(len(testInputs)):
        currentInput = testInputs[i]
        expected = expectedOutputs[i]

        # Single location where the function is executed
        # actual = solver.countAndSay(currentInput)
        # actual = solver.countAndSayV2(currentInput)
        actual = solver.countAndSayV3(currentInput)


        # Validation check
        if actual == expected:
            print(f"Test Case {i + 1}: PASSED ({currentInput} -> \"{actual}\")")
        else:
            print(f"Test Case {i + 1}: FAILED! Input: {currentInput} | Expected: \"{expected}\", but got: \"{actual}\"")