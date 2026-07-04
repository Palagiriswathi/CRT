#1636-sort array by increasing frequency

from collections import Counter
from typing import List
class solution:
    def frequenceSort(self,nums: List[int])-> List[int]:
        d=Counter(nums)
        u_d=sorted(d.items(),key=lambda x:(x[1],-x[0]))
        result=[]
        for i,j in u_d:
            for k in range(j):
                result.append(i)
        return result 
print(solution().frequenceSort([2,3,1,3,2]))
    