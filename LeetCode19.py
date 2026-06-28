from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ==========================================
# 1. IMPLEMENTATION
# ==========================================
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of the list and returns its head.
        Uses a dummy node and two pointers (fast and slow) to solve it in one pass.
        """
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # Advance fast pointer so that the gap between fast and slow is n nodes
        for _ in range(n + 1):
            if fast is None:
                return head # Edge case guard, though LeetCode guarantees valid n
            fast = fast.next
            
        # Move fast to the end, maintaining the gap
        while fast is not None:
            fast = fast.next
            slow = slow.next
            
        # slow.next is the node to be deleted
        slow.next = slow.next.next
        
        return dummy.next

    def removeNthFromEndV2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fastNode = dummy
        slowNode = dummy
        for i in range(n + 1):
            if fastNode is not None:
                fastNode = fastNode.next 
            else:
                return head
        
        while fastNode is not None:
            fastNode = fastNode.next
            slowNode = slowNode.next
            
        slowNode.next = slowNode.next.next    
            
        return dummy.next         
    
    def removeNthFromEndV3(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        for _ in range(n + 1):
            if fast is not None:
                fast = fast.next
            else:
                return head
        
        while fast is not None:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return dummy.next                     
        

# ==========================================
# 2. TEST LOGIC & HELPERS
# ==========================================

def list_to_linkedlist(arr: List[int]) -> Optional[ListNode]:
    """Helper to convert a Python list into a Linked List."""
    if not arr:
        return None
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    """Helper to convert a Linked List back into a Python list for easy assertion."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

def run_tests():
    solution = Solution()
    
    # Test cases defined as (input_list, n, expected_output_list)
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),  # Standard case: remove from middle/end
        ([1], 1, []),                        # Single node list: remove the only node
        ([1, 2], 1, [1]),                    # Two nodes: remove the last node
        ([1, 2], 2, [2]),                    # Two nodes: remove the first node (head)
        ([1, 2, 3], 3, [2, 3]),              # Remove the head from a longer list
    ]
    
    success_count = 0
    failed_count = 0
    
    print("Executing Test Cases...\n" + "-"*40)
    
    for i, (input_arr, n, expected) in enumerate(test_cases, 1):
        # Build the linked list
        head = list_to_linkedlist(input_arr)
        
        # Single execution call of the implementation per test case
        # result_head = solution.removeNthFromEnd(head, n)
        # result_head = solution.removeNthFromEndV2(head, n)
        result_head = solution.removeNthFromEndV3(head, n)        
        
        # Convert result back to standard array for verification
        result_arr = linkedlist_to_list(result_head)
        
        if result_arr == expected:
            print(f"Test Case {i}: PASSED")
            success_count += 1
        else:
            print(f"Test Case {i}: FAILED (Input: {input_arr}, n: {n} | Expected: {expected} | Got: {result_arr})")
            failed_count += 1
            
    print("-"*40)
    print(f"SUMMARY: {success_count} passed, {failed_count} failed.")

if __name__ == "__main__":
    run_tests()