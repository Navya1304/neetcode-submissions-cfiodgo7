class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for k,v in enumerate(nums):
            if target-v in h:
                return [h[target-v],k]
            h[v]=k