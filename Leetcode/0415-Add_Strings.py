class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        if len(num1) < len(num2):
            num1, num2 = num2, num1
            
        carry = 0
        result = ""
        for i in range(len(num1)):
            temp = int(num1[i]) + carry
            if i < len(num2):
                temp += int(num2[i])
            
            carry = int(temp/10)
            temp = temp%10
            result += str(temp)
        
        if carry != 0:
            result += str(carry)
            
        return result[::-1]
