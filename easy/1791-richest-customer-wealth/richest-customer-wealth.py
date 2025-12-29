class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for account in accounts:
            total = sum(account)
            
            if total > max_wealth:
                max_wealth = total
        
        return max_wealth


        