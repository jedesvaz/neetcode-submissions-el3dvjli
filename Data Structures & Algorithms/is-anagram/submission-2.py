class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        li, lis = [],[]
        if len(s) == len(t):
            for i in range(0, len(s)):
                li.append(s[i])
                lis.append(t[i])
            li.sort()
            lis.sort()
            if li == lis:
                return True
        return False

