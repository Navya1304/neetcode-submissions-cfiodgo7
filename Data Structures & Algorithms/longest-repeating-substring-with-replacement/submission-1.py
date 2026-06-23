class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        cn=0
        f={}
        for r in range(len(s)):
            f[s[r]]=f.get(s[r],0)+1
            cn=max(cn,f[s[r]])
            if r-l+1-cn>k:
                f[s[l]]-=1
                l+=1
        return r-l+1