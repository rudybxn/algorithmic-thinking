class Solution:

    def encode(self, strs: List[str]) -> str:
        # convert to one string with a delimiter thats not present within ascii 256
        encoded = ""
        for s in strs:
            encoded+=str(len(s))+"#"+s
        return encoded
#Hello, World -> 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        # search for this delimiter and expand to list
        res = []
        i = 0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            l = int(s[i:j])
            res.append(s[j+1:j+1+l])
            i=j+1+l

        return res

