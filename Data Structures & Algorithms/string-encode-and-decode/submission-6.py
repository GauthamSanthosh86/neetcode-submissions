class Solution:
#brute force
    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+"#"+i
        return s
            
            
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            sep = s.find("#", i)

            length = int(s[i:sep])

            start = sep + 1
            word = s[start:start + length]

            res.append(word)

            i = start + length

        return res