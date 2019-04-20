class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if len(T) == 0:
            return []
        
        ans = [0]
        for i in range(len(T)-2, -1, -1):
            index = i + 1
            nextVal = T[index]
            reverseIndex = len(T)-2-i
            count = 1
            while nextVal <= T[i] and ans[reverseIndex] > 0:
                count += ans[reverseIndex]
                nextVal = T[index+ans[reverseIndex]]
                index += ans[reverseIndex]
                reverseIndex -= ans[reverseIndex]
            
            if nextVal <= T[i]:
                ans.append(0)
            else:
                ans.append(count)
        
        return ans[::-1]

