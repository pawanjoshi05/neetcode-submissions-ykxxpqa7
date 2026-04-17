class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointer approach
        buy=0
        sell=1
        max_profit=0
        # buy will represent lowest 
        # sell will represent highest price
        while(sell<len(prices)):
            if(prices[sell]>prices[buy]):
                max_profit=max(max_profit,prices[sell]-prices[buy])
                sell+=1
            
            else:
                buy=sell
                sell+=1

        return max_profit