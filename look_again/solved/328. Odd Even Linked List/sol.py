# Definition for singly-linked list.

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(values: List[int]) -> Optional[ListNode]:
    """Helper function to convert a regular list to a linked list"""
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even_head = head.next
        even = even_head

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


if __name__ == "__main__":
    s = Solution()
    l_l = list_to_linked_list([1, 2, 3, 4, 5])
    print(s.oddEvenList(l_l))
