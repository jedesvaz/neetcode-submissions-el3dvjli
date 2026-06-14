class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        j = 0
        for i in range(0,len(nums)):
            
            
            if nums[i] == j and i>0:
                
                return True
            j = nums[i]
            
        return False