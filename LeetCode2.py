# LeetCode2.py

from typing import List, Optional

# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class ListNode2:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next        

class ListNode3:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head to simplify tracking the start of the result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Continue looping if there are nodes left in l1 OR l2, OR if a carry remains
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for this column position
            total_sum = val1 + val2 + carry
            
            # Calculate new carry and the digit value to store
            carry = total_sum // 10
            digit = total_sum % 10
            
            # Create new node and move the tracking pointer forward
            current.next = ListNode(digit)
            current = current.next
            
            # Move list pointers forward if they haven't reached the end
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy_head.next

    def addTwoNumbersV2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        
        return dummy.next    

    def addTwoNumbersV3(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10
            current.next = ListNode(digit)
            current = current.next
            
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        
        return  dummyHead.next   

# --- Helper Functions for Test Logic ---

def to_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Converts a Python list into a Linked List."""
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def to_python_list(node: Optional[ListNode]) -> List[int]:
    """Converts a Linked List back into a Python list for easy comparison/printing."""
    result = []
    curr = node
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

# --- Main Function with Looped Test Cases ---
if __name__ == "__main__":
    solution = Solution()
    
    # Test case group containing all scenario data
    test_cases = [
        {
            "id": 1,
            "l1": [2, 4, 3],
            "l2": [5, 6, 4],
            "expected": [7, 0, 8]
        },
        {
            "id": 2,
            "l1": [0],
            "l2": [0],
            "expected": [0]
        },
        {
            "id": 3,
            "l1": [9, 9, 9, 9, 9, 9, 9],
            "l2": [9, 9, 9, 9],
            "expected": [8, 9, 9, 9, 0, 0, 0, 1]
        }
    ]
    
    # Loop through the test case group
    for tc in test_cases:
        # Convert raw arrays into ListNode configurations
        linked_l1 = to_linked_list(tc["l1"])
        linked_l2 = to_linked_list(tc["l2"])
        
        # Call implementation function exactly once
        # actual_node_result = solution.addTwoNumbers(linked_l1, linked_l2)
        # actual_node_result = solution.addTwoNumbersV2(linked_l1, linked_l2)
        actual_node_result = solution.addTwoNumbersV3(linked_l1, linked_l2)  
        
        # Convert result node chain back to basic list formatting
        actual_list = to_python_list(actual_node_result)
        
        print(f"Test Case {tc['id']}:")
        print(f"  l1:       {tc['l1']}")
        print(f"  l2:       {tc['l2']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Actual:   {actual_list}")
        print("-" * 45)