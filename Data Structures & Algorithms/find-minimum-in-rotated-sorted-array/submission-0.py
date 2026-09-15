class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn=nums[0]
        for i in nums:
            if i<minn:
                minn=i
        return minn