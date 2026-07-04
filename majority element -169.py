#pascal triangle 
#majority element -169

def majorityElement(nums):
    c=0
    val=0
    for num in nums:
        if c==0:
            val=num
        if num==val:
            c+=1
        else:
            c-=1        
    return val