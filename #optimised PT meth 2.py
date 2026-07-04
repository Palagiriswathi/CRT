#optimised pascal triangle problem

row=int(input())
ans=1
print(ans,end=" ")
for col in range(1,row):#1,6
    ans=ans*(row-col)#T.C:-O(N)
    ans=ans//(col)
    print(ans,end=" ")