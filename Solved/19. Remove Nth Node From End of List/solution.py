# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        extra_head = ListNode()
        extra_head.next = head

        first_pointer = extra_head
        second_pointer = extra_head
        for _ in range(n + 1):
            first_pointer = first_pointer.next

        while first_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        second_pointer.next = second_pointer.next.next
        return extra_head.next


input_var = [1, 2]
n = 2

head = ListNode(input_var[0])
current = head

for input in input_var[1:]:
    current.next = ListNode(input)
    current = current.next


solution = Solution().removeNthFromEnd(head=head, n=n)
while solution:
    print(solution.val)
    solution = solution.next
