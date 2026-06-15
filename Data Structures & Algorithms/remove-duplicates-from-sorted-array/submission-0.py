class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        if k == 0:
            return 0
        if k == 1:
            return 1
        slow = 0
        for fast in range(1,len(nums)):
            if nums[slow] == nums[fast]:
                fast+=1
            else:
                slow+=1
                nums[slow] = nums[fast]
        return slow+1