class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            cn=[0]*26
            for c in s:
                cn[ord(c)-ord("a")]+=1
            res[tuple(cn)].append(s)
        return list(res.values())