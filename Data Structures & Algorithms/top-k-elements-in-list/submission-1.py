class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for n in nums:
            d[n]=d.get(n,0)+1
        f=[[] for i in range(len(nums)+1)]
        for n,v in d.items():
            f[v].append(n)
        r=[]
        for i in range(len(f)-1,-1,-1):
            for n in f[i]:
                r.append(n)
                if len(r)==k:
                    return r