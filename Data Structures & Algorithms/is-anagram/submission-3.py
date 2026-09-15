class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        c_s={}
        c_t={}
        for i in s:
            c_s[i]=c_s.get(i,0)+1

        for i in t:
            c_t[i]=c_t.get(i,0)+1
    
        return c_s==c_t