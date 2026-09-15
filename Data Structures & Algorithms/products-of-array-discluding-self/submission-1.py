class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums)) # create a list of N (length of input) 1s for final calc. 

        prefix = 1 # default the prefix to 1 for first pass

        for i in range(len(nums)): # iterate through nums list
            output[i] = prefix # set the current i equal to the prefix
            prefix *= nums[i] # new prefix equals itself * whatever number exists in nums[i]
                              # repeat this process until len(nums)

        suffix = 1 # default the suffix to 1 for second pass
        for i in range(len(nums) - 1, -1, -1): # iterate through nums in reverse
            output[i] *= suffix # set the current i equal to the suffix
            suffix *= nums[i] # new prefix equals itself * whatever number exists in nums[i]
                              # repeat this process until len(nums)
        return output
