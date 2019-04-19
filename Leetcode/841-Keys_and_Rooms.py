class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = {0}
        stack = [0]
        while len(stack) != 0:
            temp = stack.pop()
            for key in rooms[temp]:
                if key not in keys:
                    keys.add(key)
                    stack.append(key)
        
        return len(keys) == len(rooms)
