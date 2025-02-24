from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        current = head

        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node

        return new_list


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
    sorted = solution.reverseList(list1)
    print("Merged:", end=" ")
    print_linked_list(sorted)
