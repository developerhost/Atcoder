# DPでMinimum Cost For Ticketsを解く

import sys
from typing import List

days = [1,4,6,7,8,20]
costs = [2,7,15]

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        for i in range(1, 366):
            if i in days:
                dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
            else:
                dp[i] = dp[i-1]
        print(dp[365])
        print(dp)
        return dp[365]
    
if __name__ == '__main__':
    Solution().mincostTickets(days, costs)