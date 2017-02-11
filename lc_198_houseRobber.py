class Solution(object):


    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob2(nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            length = len(nums)
            if length == 0:
                return 0
            dp = []
            dp.append(0)
            dp.append(nums[0])
            for i in range(1, length):
                dp.append(max(dp[i], dp[i - 1] + nums[i]))
            return dp[length]

        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        sublist1 = list(nums[0: length - 1])
        sublist2 = list(nums[1: length])
        return max(rob2(sublist1), rob2(sublist2))

numList = [11, 2, 4, 5, 8, 9, 10]
print(Solution.rob(Solution, numList))