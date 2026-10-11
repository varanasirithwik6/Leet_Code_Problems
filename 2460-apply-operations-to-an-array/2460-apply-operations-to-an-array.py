class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] *2
                nums[i + 1] = 0

        res=[]
        for s in nums:
            if s!=0:
                res.append(s)

        while len(res) < n:
            res.append(0)
        
        return res
        