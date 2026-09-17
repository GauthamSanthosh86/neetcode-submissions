class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        max_end=nums[0]
        for i in range(1,len(nums)):
            max_end=max(max_end+nums[i],nums[i])
            res=max(max_end,res)
        return res
