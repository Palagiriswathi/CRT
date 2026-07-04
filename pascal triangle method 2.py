#they will give row number we need to print the entire row

def generateRow(row,col):
    n=row-1
    r=col-1 #T.C:-O(N**2)
    ans=1
    for i in range(r):
        ans=ans*(n-i)#numerator
        ans=ans//(i+1)#dinominator
    print(ans,end=" ")
row=int(input())           
for col in range(1,row+1):
    generateRow(row,col)
        