class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d = {0:1}
        count = 0
        curr = 0
        for n in nums:
            curr+=n
            if curr-k in d:
                count+=d[curr-k]
            if curr in d:
                d[curr]+=1
            else:
                d[curr]=1
            
        return count


            
    # ct: 4
    # d={0:1,2:2,1:1}

