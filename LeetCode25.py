from typing import List, Optional


# --- 1. Definition for singly-linked list ---
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# --- 2. Solution Implementation ---
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break

            group_next = kth.next
            prev, curr = kth.next, group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp

        return dummy.next

    def getKthNode(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseKGroupV2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        groupPre = dummy
        while True:
            # find kth node
            kth = self.getKthNode(groupPre, k)
            if not kth:
                break
            # reverse kth nodes
            groupNext = kth.next
            pre = kth.next
            current = groupPre.next
            while current != groupNext:
                temp = current.next
                current.next = pre
                pre = current
                current = temp

            # reset group pre
            temp = groupPre.next
            groupPre.next = kth
            groupPre = temp

        return dummy.next

    def reverseKGroupV3(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        groupPre = dummy

        while True:
            # get kth node
            kth = self.getKthNode(groupPre, k)

            if not kth:
                break
            # reverse kth node
            groupNext = kth.next
            pre = kth.next
            current = groupPre.next
            while current != groupNext:
                temp = current.next
                current.next = pre
                pre = current
                current = temp

            temp = groupPre.next
            groupPre.next = kth
            groupPre = temp
        return dummy.next


# --- 3. Helper Functions for Testing ---
def build_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


# --- 4. Updated Test Logic ---
def run_tests():
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
        ([1], 1, [1]),
        ([], 3, []),
        ([1, 2], 3, [1, 2]),
        ([1, 2, 3, 4], 2, [2, 1, 4, 3]),  # Exact multiple of k
    ]

    print("Running LeetCode 25: Reverse Nodes in k-Group Tests...\n")

    passed_count = 0
    failed_count = 0
    total_tests = len(test_cases)

    for i, (arr, k, expected) in enumerate(test_cases):
        head = build_linked_list(arr)
        # result_head = solution.reverseKGroup(head, k)
        # result_head = solution.reverseKGroupV2(head, k)
        result_head = solution.reverseKGroupV3(head, k)

        result_arr = linked_list_to_list(result_head)

        if result_arr == expected:
            print(
                f"✅ Test {i + 1} Passed! (k={k}) -> Input: {arr} | Output: {result_arr}"
            )
            passed_count += 1
        else:
            print(f"❌ Test {i + 1} Failed! (k={k})")
            print(f"   Input:    {arr}")
            print(f"   Expected: {expected}")
            print(f"   Got:      {result_arr}")
            failed_count += 1

    # --- Summary Dashboard ---
    print("\n" + "=" * 40)
    print("TEST RUN SUMMARY")
    print("=" * 40)
    print(f"Total Test Cases: {total_tests}")
    print(f"Passed:           {passed_count} / {total_tests}")
    print(f"Failed:           {failed_count} / {total_tests}")
    print("=" * 40)

    if failed_count == 0:
        print("🎉 Status: SUCCESS - All tests passed!")
    else:
        print("⚠️ Status: FAILURE - Review failed cases above.")


if __name__ == "__main__":
    run_tests()
