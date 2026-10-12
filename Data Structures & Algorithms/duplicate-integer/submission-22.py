class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}
        for num in nums:
        # If countMap does not contain name
            if num not in countMap:
                countMap[num] = 1
            else:
                return True
        return False