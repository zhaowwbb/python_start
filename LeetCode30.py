# LeetCode30.py

from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        
        # If the string is shorter than the combined length of all words
        if len(s) < total_len:
            return []
            
        word_freq = Counter(words)
        result = []
        
        # Run sliding window for each possible alignment offset
        for i in range(word_len):
            left = i
            right = i
            current_freq = Counter()
            count = 0
            
            while right + word_len <= len(s):
                # Extract the next word candidate
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_freq:
                    current_freq[word] += 1
                    count += 1
                    
                    # If we have more occurrences of 'word' than required, shrink from the left
                    while current_freq[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        count -= 1
                        left += word_len
                        
                    # If the number of matching words matches the total words required
                    if count == word_count:
                        result.append(left)
                else:
                    # Word not in dictionary, reset window entirely
                    current_freq.clear()
                    count = 0
                    left = right
                    
        return result

    def findSubstringV2(self, s: str, words : List[str]) -> List[int]:
        # result = []
        # print(f"s={s}")
        # print(f"words={words}")
    
        if not s or not words:
            return []
        if len(s) == 0 or len(words) == 0:
            return []
        word_len = len(words[0])
        word_count = len(words)
        word_freq = Counter(words)
        result = []
        # print(f"word_len={word_len}")
        # print(f"word_count={word_count}")
        
        for i in range(word_len):
            left, right = i, i
            current_freq = Counter()
            count = 0
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                if word in word_freq:
                    current_freq[word] += 1
                    count += 1
                    # print(current_freq, count, left, right)
                    while current_freq[word] > word_freq[word]:
                        leftWord = s[left: left + word_len]
                        current_freq[leftWord]  -=  1
                        count -= 1
                        left += word_len
                    
                    if count == word_count:
                        result.append(left)    
                else:
                    current_freq.clear()
                    count = 0
                    left = right
                                
        return result

    def findSubstringV3(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        word_freq = Counter(words)                
        result = []
        
        for i in range(word_len):
            left, right = i, i
            current_freq = Counter()
            count = 0
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                if word in word_freq:
                    current_freq[word] += 1
                    count += 1
                    while current_freq[word] > word_freq[word]:
                        leftWord = s[left: left + word_len]
                        current_freq[leftWord] -= 1
                        count -= 1
                        left += word_len                        
                    if count == word_count:
                        result.append(left)                    
                else:
                    current_freq.clear()
                    count = 0
                    left = right    
                
        return result

# --- Main Function with Looped Test Cases ---
if __name__ == "__main__":
    solution = Solution()
    
    # Test case group containing all scenario data
    test_cases = [
        {
            "id": 1,
            "s": "barfoothefoobarman",
            "words": ["foo", "bar"],
            "expected": [0, 9]
        },
        {
            "id": 2,
            "s": "wordgoodgoodgoodbestword",
            "words": ["word", "good", "best", "word"],
            "expected": []
        },
        {
            "id": 3,
            "s": "barfoofoobarthefoobarman",
            "words": ["bar", "foo", "the"],
            "expected": [6, 9, 12]
        },
        {
            "id": 4,
            "s": "wordgoodgoodgoodbestword",
            "words": ["word", "good", "best", "good"],
            "expected": [8]
        }
    ]
    
    # Loop through the test case group
    for tc in test_cases:
        # Call implementation function exactly once
        # actual_result = solution.findSubstring(tc["s"], tc["words"])
        # actual_result = solution.findSubstringV2(tc["s"], tc["words"])
        actual_result = solution.findSubstringV3(tc["s"], tc["words"])
        
        print(f"Test Case {tc['id']}:")
        print(f"  s:        '{tc['s']}'")
        print(f"  words:    {tc['words']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Actual:   {actual_result}")
        print("-" * 40)