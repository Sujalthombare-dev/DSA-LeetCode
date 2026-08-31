class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in range(len(s)):
            if i==0:
                stack.append(s[i])
            elif s[i] in stack:
                return s[i]
            stack.append(s[i])

        