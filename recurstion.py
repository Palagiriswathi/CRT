#function calling itself until it reaches its base condition  it is recurstion 
# how it works (first it goes deep left then it slowly goes through the right
# if index is out of array--> if(ind(arr))

def generate(ind,curr_subset,ans,nums):
    if (ind==len(nums)):
        ans.append(curr_subset.copy())
        return
    curr_subset.append(nums[ind])
    generate(ind+1,curr_subset,ans,nums)
    curr_subset.pop()
    generate(ind+1,curr_subset,ans,nums)
def subsets(nums):
    curr_subset=[]
    ans=[]
    ind=0
    generate(ind,curr_subset,ans,nums)
    return ans
arr=[1,2,3]
print(subsets(arr))        
    