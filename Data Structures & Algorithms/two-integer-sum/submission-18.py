class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        licopy = []
        for i, num in enumerate(nums):
            licopy.append([num, i])

        licopy.sort( reverse=True)
        i, j = 0, len(licopy)-1

        while i<j:
            if licopy[i][0] + licopy[j][0] == target:
                

                return [min(licopy[i][1], licopy[j][1]), max(licopy[i][1], licopy[j][1])]
            elif licopy[i][0] + licopy[j][0] > target: 
                i+=1
            else:
                j-=1