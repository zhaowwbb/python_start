from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swaps every two adjacent nodes in a linked list and returns its head.
        Time Complexity: O(N) - We traverse the list exactly once.
        Space Complexity: O(1) - Constant space scaling.
        """
        # Create a dummy node to ease edge cases at the head of the list
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Ensure there are at least two nodes left to swap
        while prev.next and prev.next.next:
            # Identify the two nodes to be swapped
            first = prev.next
            second = prev.next.next

            # Perform the swap by altering pointers
            first.next = second.next
            second.next = first
            prev.next = second

            # Advance the prev pointer forward by two nodes for the next iteration
            prev = first

        return dummy.next

    def swapPairsV2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        first = head
        second = head.next if first else None
        while first and second:
            temp = second.next if second.next else None

            current.next = second
            current = current.next
            current.next = first
            current = current.next
            if temp is None:
                current.next = None
                return dummy.next

            current.next = temp

            first = current.next
            if first:
                second = first.next

        if first:
            current.next = first
            current.next.next = None

        return dummy.next

    def swapPairsV3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            first.next = second.next
            prev.next = second
            second.next = first

            prev = first

        return dummy.next


# ==========================================
# TEST HELPER FUNCTIONS
# ==========================================


def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Helper to convert a standard Python list to a linked list."""
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Helper to convert a linked list back to a standard Python list for verification."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ==========================================
# TEST LOGIC
# ==========================================
if __name__ == "__main__":
    solution = Solution()

    # Define test cases: (input_list, expected_swapped_list)
    test_cases = [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [2, 1, 3]),
        ([7, 9, 2, 8, 3], [9, 7, 8, 2, 3]),
    ]

    success_count = 0
    failed_count = 0

    print("Running Tests for Swap Nodes in Pairs...")
    print("-" * 50)

    for i, (raw_list, expected) in enumerate(test_cases):
        # Convert raw arrays into ListNode setup
        head = create_linked_list(raw_list)

        # Run implementation
        # swapped_head = solution.swapPairs(head)
        # swapped_head = solution.swapPairsV2(head)
        swapped_head = solution.swapPairsV3(head)        

        actual = linked_list_to_list(swapped_head)

        if actual == expected:
            print(f"Test Case {i + 1}: PASSED")
            success_count += 1
        else:
            print(f"Test Case {i + 1}: FAILED")
            print(f"  Expected: {expected}")
            print(f"  Got:      {actual}")
            failed_count += 1

    print("-" * 50)
    print(f"Total Successes: {success_count}")
    print(f"Total Failures:  {failed_count}")
