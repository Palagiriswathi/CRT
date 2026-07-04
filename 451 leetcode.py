#451-leetcode

from collections import Counter
class solutions:
    def frequencesort(self,s:str)->str:
        d=Counter(s)
        u_d=sorted(d.items(),key=lambda x:-x[1])
        result=" "
        for i,j in u_d:
            result+=i*j
        return result
print(solutions().frequencesort("tree"))