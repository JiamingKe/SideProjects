class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        sign = num > 0
        num = abs(num)
        result = ""
        
        while num != 0:
            result = str(num % 7) + result
            num = int(num/7)
        
        if not sign:
            result = "-" + result
        return result
