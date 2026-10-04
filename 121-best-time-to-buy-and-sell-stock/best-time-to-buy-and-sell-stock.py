class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        nums=[]
        low=prices[0]
        for i in range(0,len(prices)):
            if prices[i]>low:
                dif=prices[i]-low
                nums.append(dif)
            else:
                low=prices[i]
        if len(nums)>0:
            return max(nums)
        else:
            return 0









        # for i in range(0,len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[j]>prices[i]:
        #             dif=prices[j]-prices[i]
        #             nums.append(dif)
        # if len(nums)>0:
        #     return max(nums)
        # else:
            # return 0