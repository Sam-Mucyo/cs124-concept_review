class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        drawing: https://docs.google.com/drawings/d/1Ooo1Ahz4SKyg4_lsjx_QQMs9YIhSL0HFnTZTpCmbHgA/edit

        Optimize of the below solution's Space complexity to just O(sum(nums))
        still: O(sum(nums) * n) time
        '''
        if sum(nums) % 2: return False

        total, n = sum(nums) // 2, len(nums)
         # Initialize the DP array
        dp = [False] * (total + 1)
        dp[0] = True  # Base case: A sum of 0 is always achievable

        # Iterate through the numbers
        for num in nums:
            # Iterate backward to avoid overwriting
            for j in range(total, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[total]


    def canPartitionTabulation(self, nums: List[int]) -> bool:
        '''
        drawing: https://docs.google.com/drawings/d/1Ooo1Ahz4SKyg4_lsjx_QQMs9YIhSL0HFnTZTpCmbHgA/edit
        with DP bottom-up approach/tabulation
        O(sum(nums) * n) both space and time
        '''
        if sum(nums) % 2: return False

        total, n = sum(nums) // 2, len(nums)

        dp = [[False] * (total + 1) for _ in range(n + 1)]

        # base case: can achieve the sum of 0 by including 0
        dp[0][0] = True

        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                not_include = dp[i - 1][j]
                include = j >= nums[i - 1] and dp[i - 1][j - nums[i - 1]]
                dp[i][j] =  include or not_include

        return dp[n][total]

    def canPartitionWithMemo(self, nums: List[int]) -> bool:
        '''
        Improve the decision tree solution below with Memoization

        O(sum(nums) * n) both space and time
        '''
        if sum(nums) % 2: return False

        total = sum(nums) / 2
        memo = {}

        def can_sum(target, i):
            if (target, i) in memo: return memo[(target, i)]
            if target == 0: return True
            if i == len(nums) or target < 0: return False

            ans = (
                can_sum(target - nums[i], i + 1) or \
                can_sum(target, i + 1)
            )
            memo[target, i] = ans
            return ans

        return can_sum(total, 0)


    def canPartitionDecisionTree(self, nums: List[int]) -> bool:
        '''
        drawing: https://docs.google.com/drawings/d/1Ooo1Ahz4SKyg4_lsjx_QQMs9YIhSL0HFnTZTpCmbHgA/edit
        Time: O(2^n)
              explore every possible subset of the array;
              For every number, either include it in the subset
              or skip it, resulting in a binary tree of possibilities.

        Space: O(n): tree depth == stack depth
        '''
        if sum(nums) % 2: return False

        total = sum(nums) / 2

        def can_sum(target, i):
            if target == 0: return True
            if i == len(nums) or target < 0: return False
            return (
                can_sum(target - nums[i], i + 1) or \
                can_sum(target, i + 1)
            )

        return can_sum(total, 0)