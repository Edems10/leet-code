from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head_holder = ListNode()
        current = head_holder

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next
            current = current.next

        while list1:
            current.next = ListNode(list1.val)
            current = current.next
            list1 = list1.next

        while list2:
            current.next = ListNode(list2.val)
            current = current.next
            list2 = list2.next

        return head_holder.next


def create_list_nodes(sequence) -> ListNode:
    """Create a linked list from a sequence of numbers."""
    dummy = ListNode()
    current = dummy
    for number in sequence:
        current.next = ListNode(number)
        current = current.next
    return dummy.next


def print_linked_list(list_node: ListNode) -> None:
    """Print all values in a linked list."""
    current = list_node
    values = []
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))


if __name__ == "__main__":
    list1 = create_list_nodes([1, 4])
    list2 = create_list_nodes([1, 3])

    print("List 1:", end=" ")
    print_linked_list(list1)
    print("List 2:", end=" ")
    print_linked_list(list2)

    solution = Solution()
    merged = solution.mergeTwoLists(list1, list2)
    print("Merged:", end=" ")
    print_linked_list(merged)
