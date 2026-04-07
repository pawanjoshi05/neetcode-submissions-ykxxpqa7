class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i=0
        j=i+1
        length=len(nums)
        if(length==0 or length==1):
            return False
        while(j<len(nums)):
            if(nums[i]==nums[j]):
                return True
            
          
            else:
                i=i+1
                j=j+1

        return False;