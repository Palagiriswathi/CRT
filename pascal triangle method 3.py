#-->given row number print pascal triangle of given rows

def generateRow(row,col):
    n=row-1
    r=col-1
    ans=1
    for i in range(r):
        ans=ans*(n-i)#numerator
        ans=ans//(i+1)#dinominator
    print(ans,end=" ")
n=int(input())
for row in range(1,n+1):
    for col in range(1,row+1):
        generateRow(row,col)
    print()    