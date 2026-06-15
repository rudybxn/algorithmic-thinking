class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1
                k-=1
        
        l = 0
        r = len(nums)-1
        print(nums)
        while nums[r]==-1 and r>=0:
            r -=1

        while l<=r:
            if nums[l] == -1:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
                while nums[r]==-1 and r>=l:
                    r-=1
            else:
                l+=1
            
        return k
