class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            # First looking for existing numbers
            if num  in seen:
                return True
            #Then add new numbers
            seen.add(num)
        return False
        