class Solution:
    def longestPalindrome(self, s: str) -> str:
        # longest = 0
        # ans = ""
        # if len(s) == 1:
        #     return s

        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         substr = s[i:j]
        #         if substr == substr[::-1]:
        #             if len(substr)>longest:
        #                 longest = len(substr)
        #                 ans = substr
        # if ans!="":
        #     return ans

        # expand around center
        # ans = ""

        # # for each index, treat it as center and check if palindrome for both even and odd versions
        # for i in range(len(s)):
        #     # for odd
        #     l=i
        #     r=i
        #     while l>=0 and r<len(s) and s[l] == s[r]:
        #         substr = s[l:r+1]
        #         if len(substr)>len(ans):
        #             ans = substr
        #         l-=1
        #         r+=1 # expand
            
        #     # for even
        #     l = i
        #     r = i+1
        #     while l>=0 and r<len(s) and s[l] == s[r]:
        #         substr = s[l:r+1]
        #         if len(substr)>len(ans):
        #             ans = substr
        #         l-=1
        #         r+=1 # expand
        
        # return ans

        # dp approach
        memo = {}
        ans = ""

        def isPalindrome(i,j)->bool:
            if i>=j:
                return True
            
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = s[i] == s[j] and isPalindrome(i+1,j-1)
            return memo[(i,j)]


        for length in range(len(s), 0, -1):
            for i in range(len(s) - length + 1):
                j = i + length - 1

                if isPalindrome(i, j):
                    return s[i:j + 1]
        


        