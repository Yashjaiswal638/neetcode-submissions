class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        c = {}
        for c1 in s:
            c[c1] = c.get(c1, 0)+1
        for c2 in t:
            c[c2] = c.get(c2, 0)-1
        for v in c.values():
            if v != 0:
                return False
        return True