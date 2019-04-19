class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = [[0]]
        ans = []
        while len(stack) != 0:
            path = stack.pop()
            for node in graph[path[-1]]:
                if node == len(graph)-1:
                    ans.append(path + [node])
                else:
                    stack.append(path + [node])
                    
        return ans
