class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs=nums[0]
        curr=0
        for num in nums:
            if curr<0:
                curr=0
            curr+=num
            maxs=max(maxs,curr)
        return maxs