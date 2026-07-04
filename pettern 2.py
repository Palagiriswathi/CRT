n=int(input())
for row in range(n):
    #spaces
    for col in range(row):
        print(" ",end=" ")
    #stars    
    for col in range(2*(n-row)-1):
        print("*",end=" ")
    print()    