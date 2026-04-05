class Solution():
    def twoSum(self, nums,target):

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j] == target):
                    print(i,j)
                    return
        print("no solution")

obj=Solution()
obj.twoSum(nums=[2,7,11,15],target=9)
