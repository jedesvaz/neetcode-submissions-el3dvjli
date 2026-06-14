class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        j = 0
        for i in range(0,len(nums)):
            print(j)
            
            if nums[i] == j and i>0:
                print(nums[i])
                return True
            j = nums[i]
            
        return False