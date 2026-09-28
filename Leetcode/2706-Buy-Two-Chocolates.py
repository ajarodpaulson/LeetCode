class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        
        leftover_money = money - (prices[0] + prices[1])

        return leftover_money if leftover_money >= 0 else money