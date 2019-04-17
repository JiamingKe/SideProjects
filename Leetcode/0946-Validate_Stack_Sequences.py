class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        indexPush = 0
        indexPop = 0
        stack = []
        
        while True:
            if indexPop == len(popped):
                return True
            
            if popped[indexPop] in pushed[indexPush:]:
                stack.append(pushed[indexPush])
                indexPush += 1
            else:
                if stack[-1] != popped[indexPop]:
                    return False
                
                indexPop += 1
                stack.pop()
