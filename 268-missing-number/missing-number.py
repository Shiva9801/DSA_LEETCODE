class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result=[]
        n=len(nums)
        
        # for i in range(n+1):            
        #     result.append(i) 
        
        # for element in result:
        #     if element not in nums:                
        #         return element


        #2nd 
        # for i in range(n+1):
        #     result.append(i)
        # x=sum(result)-sum(nums)
        # return x

        #3rd here we use ap formula of nth numbers sums
        expect=n*(n+1)//2
        actual=sum(nums)
        return expect-actual



