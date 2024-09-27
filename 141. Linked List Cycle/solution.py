
from typing import Optional


class ListNode:
    def __init__(self,x) -> None:
        self.val = x
        self.next = None
        
        
class Solution:
    def __init__(self) -> None:
        self.visited_list = set()
        
    def hasCycle(self, head: Optional[ListNode])->bool:
        if not head:
            return
        self.visited_list.add(head)
        current = head.next
        while(current):
            if not current in self.visited_list:
                self.visited_list.add(current)
                current = current.next
            else:
                return True
        return False
    
    