class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_cn={}
        t_cn={}
        for i in range(len(s)):
            s_cn[s[i]]=1+s_cn.get(s[i],0)
            t_cn[t[i]]=1+t_cn.get(t[i],0)
        return s_cn==t_cn