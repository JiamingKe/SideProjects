# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lowerbound = 1
        upperbound = n
        while lowerbound + 1 < upperbound:
            mid = (lowerbound + upperbound)/2
            resp = guess(mid)
            if resp == 0:
                return mid
            
            if resp == 1:
                lowerbound = mid
            else:
                upperbound = mid
