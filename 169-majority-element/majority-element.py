class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        #1st apporach
        # for i in range(len(nums)):
        #     count=0

        #     for j in range(len(nums)):
        #         if nums[j]==nums[i]:
        #             count+=1
            
        #     if count>len(nums)/2:
        #         return nums[i]
        # 2nd approach
        nums.sort()
        return nums[len(nums)//2]
        #3rd approach
        # n=len(nums)
        # for i in range(n-1):
        #     for j in range(n-i-1):
        #         if nums[j]>nums[j+1]:
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        # return nums[n//2]