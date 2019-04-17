import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        heap = []
        result = []
        
        for val in nums:
            if table.get(val) is None:
                table[val] = 0
            else:
                table[val] += 1
        
        for key in table:
            heap.append((-table[key], key))
        
        heapq.heapify(heap)
        
        for i in range(k):
            pair = heapq.heappop(heap)
            result.append(pair[1])
        
        return result
