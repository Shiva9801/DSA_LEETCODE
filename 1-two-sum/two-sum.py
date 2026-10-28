class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i,x in enumerate(nums):
            partner=target-x
            if partner in seen:
                return [seen[partner],i]
            seen[x]=i
        return None
