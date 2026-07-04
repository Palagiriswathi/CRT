# pascal triangle
#-->they will give u row &col and need to print element
#ncr=row-1c col-1
#row=6,col=4
#5c3=5!/3!*2!=10 -->n-i/i+1

row=int(input())
col=int(input())
n=row-1
r=col-1
ans=1
for i in range(r):
    ans=ans*(n-i)#numerator
    ans=ans//(i+1)#dinominator
print(ans)    

