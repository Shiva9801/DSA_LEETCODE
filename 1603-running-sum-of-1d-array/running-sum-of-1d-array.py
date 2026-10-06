class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total=0
        list=[]
        for i in range(len(nums)):
            total=total+nums[i]
            list.append(total)
        return list
            
            

        #older approach 
        # total=0
        # result=[]
        # for i in nums:
        #     total=total+i
        #     result.append(total)

        # return result
