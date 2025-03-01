from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def grab_keys(current_keys: deque, keys: List) -> deque[int]:
            for key in keys:
                if key not in current_keys and key not in visited:
                    current_keys.append(key)
            return current_keys

        visited = deque([0])
        aquired_keys = grab_keys(deque([]), rooms[0])
        visited_count = 1
        while len(visited) < len(rooms) and len(aquired_keys) > 0:
            key = aquired_keys.popleft()
            visited.append(key)
            visited_count += 1
            aquired_keys = grab_keys(aquired_keys, rooms[key])
        if visited_count == len(rooms):
            return True
        else:
            return False


if __name__ == "__main__":
    rooms = [[1], [2], [3], []]
    s = Solution()
    outcome = s.canVisitAllRooms(rooms)
    print(outcome)
