import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # We need to define a less-than (<) operator for the Min-Heap.
    # If two nodes have the same value, we break the tie arbitrarily (by memory address or ID).
    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists into one sorted linked list.
        Time Complexity: O(N log k) where N is total nodes, k is number of lists.
        Space Complexity: O(k) for the priority queue.
        """
        min_heap = []

        # Step 1: Push the head of each non-empty list into the heap
        # We store tuples: (node_value, list_index, node_object) to safely avoid comparison crashes
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))

        dummy = ListNode(0)
        current = dummy

        # Step 2: Extract the minimum element and push its next element
        while min_heap:
            val, i, node = heapq.heappop(min_heap)

            # Append to the merged list
            current.next = node
            current = current.next

            # If there is a next node in that same list, push it to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next

    def mergeKListsV2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(minHeap, (head.val, i, head))

        dummy = ListNode(0)
        current = dummy

        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))

        return dummy.next

    def mergeKListsV3(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(minHeap, (head.val, i, head))

        dummy = ListNode(0)
        current = dummy
        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))

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
    """Helper to convert a linked list back to a standard Python list for testing."""
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

    # Define test cases: (input_lists, expected_flat_list)
    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1, 3, 5, 7], [2, 4, 6, 8]], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([[-1, 5, 11], [], [6, 10]], [-1, 5, 6, 10, 11]),
    ]

    success_count = 0
    failed_count = 0

    print("Running Tests for Merge k Sorted Lists...")
    print("-" * 50)

    for i, (raw_lists, expected) in enumerate(test_cases):
        # Convert raw arrays into ListNode configurations
        linked_lists = [create_linked_list(arr) for arr in raw_lists]

        # Run implementation
        # merged_head = solution.mergeKLists(linked_lists)
        # merged_head = solution.mergeKListsV2(linked_lists)
        merged_head = solution.mergeKListsV3(linked_lists)

        actual = linked_list_to_list(merged_head)

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
