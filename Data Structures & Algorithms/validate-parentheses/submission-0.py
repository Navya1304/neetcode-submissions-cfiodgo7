class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        mapp={')':'(','}':'{',']':'['}
        for i in s:
            if i in mapp.values():
                st.append(i)
            elif i in mapp.keys():
                if not st or mapp[i]!=st.pop():
                    return False
        return not st