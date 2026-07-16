class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>len(s):
            return s
        rows=[""]*numRows
        curr=0
        d=-1
        for ch in s:
            rows[curr]+=ch
            if curr==0 or curr==numRows-1:
                d*=-1
            curr+=d
        return "".join(rows) 