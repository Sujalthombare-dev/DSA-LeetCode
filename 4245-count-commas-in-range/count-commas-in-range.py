class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n>=1000:
            return 1+(n-1000)
        else:
            return 0
        