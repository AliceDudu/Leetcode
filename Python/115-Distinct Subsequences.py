
class Solution(object):
    def numDistinct(self, s, t):
        
        dp = [[0 for j in range(len(s)+1)] for i in range(len(t)+1) ]
        
        for j in range(len(s)+1):
            dp[0][j] = 1
        
        for i in range(len(t)):
            for j in range(len(s)):
                if t[i]==s[j]:
                    dp[i+1][j+1] = dp[i+1][j] + dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]
        
        return dp[len(t)][len(s)]
