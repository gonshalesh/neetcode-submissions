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

'''
Demo:

Starting nums list = [1, 2, 4, 6]
Starting Output = [1, 1, 1, 1]
Default Prefix = 1

1st Pass:
prefix = 1 (from default prefix)
output[0] = prefix (output[0] which was 1 now equals 1)
prefix = prefix * nums[0] (1 * 1 = 1)

New Output List = [1, 1, 1, 1]
New Prefix = 1

2nd Pass:
prefix = 1 (from 1st pass)
output[1] = prefix (output[1] which was 1 now equals 1)
prefix = prefix * nums[1] (1 * 2 = 2)

New Output List = [1, 1, 1, 1]
New Prefix = 2

3rd Pass:
prefix = 2 (from 2nd pass)
output[2] = prefix (output[2] which was 1 now equals 2)
prefix = prefix * nums[2] (2 * 4 = 8)

New Output List = [1, 1, 2, 1]
New Prefix = 8

4th Pass:
prefix = 8
output[3] = prefix (output[3] which was 1 now equals 8)

* loop terminates, no more numbers left in len(nums) *
New Output List = [1, 1, 2, 8]

* backwords loop begins *
Starting nums list = [1, 2, 4, 6]
Starting Output = [1, 1, 2, 8] (from last pass in first loop)
Default suffix = 1
Iteration order: Reverse

1st Pass:
suffix = 1 (from default suffix)
output[3] = output[3] * suffix (output[3] which was 8 now equals 8)
suffix = suffix * nums[3] (1 * 6 = 6)

New Output List = [1, 1, 2, 8]
New Suffix = 6

2nd Pass:
suffix = 6 (from 1st pass)
output[2] = output[2] * suffix (2 * 6 = 12)
suffix = suffix * nums[2] (6 * 4 = 24)

New Output List = [1, 1, 12, 8]
New Suffix = 24

3rd Pass:
suffix = 24 (from 2nd pass)
output[1] = output[1] * suffix (1 * 24 = 24)
suffix = suffix * nums[1] (24 * 2 = 48)

New Output List = [1, 24, 12, 8]
New Suffix = 48

4th Pass:
suffix = 48 (from 3rd pass)
output[0] = output[0] * suffix (1 * 48 = 48)

* loop terminates, no more numbers left in reverse *

Final Output List = [48, 24, 12, 8]

'''
