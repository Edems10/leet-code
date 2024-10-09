from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:

    def fill_first_values(self, lists: List[Optional[ListNode]]):
        list_ended = False
        current_values = {}
        list_iterator = 0
        while list_ended != True:
            if lists[list_iterator] != None:
                current_number = lists[list_iterator].val
                current_values[list_iterator] = current_number
            list_iterator += 1
            if list_iterator == len(lists):
                list_ended = True
        return current_values

    def check_empty_list(self, lists: List[Optional[ListNode]]):
        if len(lists) == 0:
            return False
        for list in lists:
            if list != None:
                if type(list.val) == int:
                    return True
        return False

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not self.check_empty_list(lists):
            return
        merged_head_dummy = ListNode()
        current_head = merged_head_dummy
        current_values = self.fill_first_values(lists)

        while current_values != {}:
            min_index = min(current_values, key=current_values.get)
            current_head.next = ListNode(current_values[min_index])
            current_head = current_head.next
            lists[min_index] = lists[min_index].next
            if lists[min_index] != None:
                current_values[min_index] = lists[min_index].val
            else:
                current_values.pop(min_index)
        return merged_head_dummy.next


def main():
    tests = [[], [1]]
    heads = []

    # Create linked lists for each test case
    for test in tests:
        head = ListNode()  # Dummy head
        current = head
        for number in test:
            current.next = ListNode(number)
            current = current.next
        heads.append(head.next)

    solution = Solution()
    merged_list = solution.mergeKLists(heads)

    # Function to print the merged linked list
    def print_linked_list(node):
        while node:
            print(node.val, end=" -> " if node.next else "\n")
            node = node.next

    print_linked_list(merged_list)


if __name__ == "__main__":
    main()
