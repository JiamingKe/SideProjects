class Solution:
    def frequencySort(self, s: str) -> str:
        table = {}
        for c in s:
            if table.get(c) is None:
                table[c] = 1
                continue
            table[c] += 1
            
        array = []
        for key in table:
            array.append(key*table[key])
            index = len(array) - 1
            for i in range(len(array)):
                if len(array[index]) >= len(array[i]):
                    index = i
                    break
            temp = array[-1]
            array[index+1:] = array[index:-1]
            array[index] = temp
                
        return "".join(subString for subString in array)

