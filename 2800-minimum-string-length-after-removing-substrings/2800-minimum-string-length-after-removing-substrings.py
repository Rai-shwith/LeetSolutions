class Solution:
    def minLength(self, s: str) -> int:
        count: int = 0
        st: list[str] = []
        for i in s:
            if i == 'A':
                st.append('B')
            elif i == 'C':
                st.append('D')
            elif st and i == st[-1]:
                st.pop()
                count-=2
            else:
                st.clear()
            count+=1
        return count