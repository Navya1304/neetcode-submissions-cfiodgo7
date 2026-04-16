class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=defaultdict(int)
        dp[0]=1
        for i in nums:
            res=defaultdict(int)
            for tot,cn in dp.items():
                res[tot+i]+=cn
                res[tot-i]+=cn
            dp=res
        return dp[target]