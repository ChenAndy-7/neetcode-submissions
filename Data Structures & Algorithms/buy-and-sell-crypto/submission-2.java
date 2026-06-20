class Solution {
    public int maxProfit(int[] prices) {
        int m_profit = 0;
        int r = 1, l = 0; 
        while (r < prices.length) {
            if (prices[l] < prices[r]) {
                int profit = prices[r] - prices[l];
                m_profit = Math.max(m_profit, profit);
            } else {
                l = r;
            }
            r++;
        }
        return m_profit;
    }
    
}
