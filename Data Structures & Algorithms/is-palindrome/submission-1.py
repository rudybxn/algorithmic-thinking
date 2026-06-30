class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().strip()
        if len(s)==0:
            return True
        l = 0
        r = len(s)-1

        while l<=r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l] == s[r]:
                    l+=1
                    r-=1
            else:
                return False
        return True
                
                
