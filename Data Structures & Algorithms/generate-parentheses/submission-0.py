class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def backtrack(open1,closed):
            if open1==closed==n:
                res.append(''.join(stack))
                return
            if open1<n:
                stack.append("(")
                backtrack(open1+1,closed)
                stack.pop()
            if closed<open1:
                stack.append(")")
                backtrack(open1,closed+1)
                stack.pop()
        backtrack(0,0)
        return res