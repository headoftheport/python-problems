class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [0 for i in range(len(nums))]
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            ans[i] = product
        product = 1;    
        for i in range(len(nums)-1,0,-1):
            ans[i] = ans[i-1] * product
            product = product * nums[i]
            
        ans[0] = product
        return ans


    def  productExceptSelf2(self, nums: List[int]) -> List[int]:


        ans, pre, post = [1 for i in range(len(nums))], 1, 1

        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]
            ans[-1-i] *= post
            post *= nums[-1-i]

        return ans


            