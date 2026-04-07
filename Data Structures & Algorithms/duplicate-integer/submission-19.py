class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # using hashmap
        maps={}
        # key and values pairs
        for i in nums:
          maps[i]=maps.get(i,0)+1
        # now looping and checking through map
        for i in nums:
            curr=i
            if(maps.get(curr,0)>1):
               return True
        return False
