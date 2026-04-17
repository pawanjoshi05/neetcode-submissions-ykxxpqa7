class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        answer=0
        n=len(prices)
        for i in range(n):
            for j in range(n):
                cp=prices[i]
                sp=prices[j]
                if(j>i):
                    profit=sp-cp
                    answer=max(profit,answer)


        return answer