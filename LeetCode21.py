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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into one continuous sorted linked list.
        """
        # Create a dummy node to hold the start of the merged list
        dummy = ListNode(-1)
        tail = dummy

        # Traverse both lists until one of them runs out
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Append the remaining nodes of whichever list is not empty
        tail.next = list1 if list1 else list2

        return dummy.next

    def mergeTwoListsV2(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2

        return dummy.next

    def mergeTwoListsV3(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2

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
    """Helper to convert a Linked List back into a Python list."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


def run_tests():
    solution = Solution()

    # Test cases defined as (list1_arr, list2_arr, expected_output_arr)
    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),  # Standard case with duplicates
        ([], [], []),  # Both lists empty
        ([], [0], [0]),  # One list empty
        (
            [1, 5, 9],
            [2, 3, 4, 6, 7],
            [1, 2, 3, 4, 5, 6, 7, 9],
        ),  # Alternating elements of varying sizes
    ]

    success_count = 0
    failed_count = 0

    print("Executing Test Cases...\n" + "-" * 40)

    for i, (arr1, arr2, expected) in enumerate(test_cases, 1):
        # Generate pristine linked lists per iteration
        l1 = list_to_linkedlist(arr1)
        l2 = list_to_linkedlist(arr2)

        # Call the implementation exactly once per test case
        # result_head = solution.mergeTwoLists(l1, l2)
        # result_head = solution.mergeTwoListsV2(l1, l2)
        result_head = solution.mergeTwoListsV3(l1, l2)

        # Convert back to standard array for assertion
        result_arr = linkedlist_to_list(result_head)

        if result_arr == expected:
            print(f"Test Case {i}: PASSED")
            success_count += 1
        else:
            print(
                f"Test Case {i}: FAILED (L1: {arr1}, L2: {arr2} | Expected: {expected} | Got: {result_arr})"
            )
            failed_count += 1

    print("-" * 40)
    print(f"SUMMARY: {success_count} passed, {failed_count} failed.")


if __name__ == "__main__":
    run_tests()
