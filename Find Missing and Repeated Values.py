class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq={}
        n=len(grid)
        for row in grid:
            for ele in row:
                if ele in freq:
                    freq[ele]+=1
                else:
                    freq[ele]=1
        for i in range(1,(n*n)+1):
            if i in freq:
                if freq[i]==2:
                    repeated=i
            else:
                missing=i
        return [repeated,missing]