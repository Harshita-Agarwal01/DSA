class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Brute Force sol
        # TC=O(N**2)  SC=O(1)
        """maxprofit=0
        profit=0
        n=len(prices)
        for i in range(n):
            for j in range(i+1,n):
                profit=prices[j]-prices[i]
                if profit>maxprofit:
                    maxprofit=profit
        return maxprofit"""

        # Better sol: Two Pass
        # TC=O(N)   SC=O(1)
        """sell=0
        n=len(prices)
        for i in range(1,n):
            if prices[i]<prices[sell]:
                sell=i
        if sell==-1:
            return 0
        profit=0
        
        for i in range(sell+1,n):
            ans=prices[i]-prices[sell]
            if ans>profit:
                profit=ans
        return profit"""

        # Optimal sol: One Pass
        # TC=O(N)   SC=O(1)
        max_profit=0
        min_price= float("inf")
        n=len(prices)
        for i in range(n):
            if prices[i]<min_price:
                min_price=prices[i]
            profit=prices[i]-min_price
            if profit>max_profit:
                max_profit=profit
        return max_profit