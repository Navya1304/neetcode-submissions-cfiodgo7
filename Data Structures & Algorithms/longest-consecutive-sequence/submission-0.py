class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cn=0
        numSet=set(nums)
        for i in numSet:
            if i-1 not in numSet:
                curr=i
                length=1
                while curr+1 in numSet:
                    curr+=1
                    length+=1
                cn=max(cn,length)
        return cn