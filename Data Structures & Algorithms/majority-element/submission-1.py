class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=cn=0
        for i in nums:
            if cn==0:
                res=i
            cn+=(1 if i==res else -1)
        return res