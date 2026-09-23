class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        l=res=0
        for r in range(len(s)):
            d[s[r]]=d.get(s[r], 0)+1
            w_length=r-l+1
            rep=w_length-max(d.values())
            if rep>k:
                d[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res