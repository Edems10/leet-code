from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        vals.sort()
        return create_list_nodes(vals)


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
    list1 = create_list_nodes([1, 22, -1, 4])

    print("List 1:", end=" ")
    print_linked_list(list1)
    solution = Solution()
    sorted = solution.sortList(list1)
    print("Merged:", end=" ")
    print_linked_list(sorted)
