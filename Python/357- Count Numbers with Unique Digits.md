### 题目：
https://leetcode.com/problems/count-numbers-with-unique-digits/

>Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

>Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

>Hint:

>A direct way is to use the backtracking approach.
Backtracking should contains three states which are (the current number, number of steps to get that number and a bitmask which represent which number is marked as visited so far in the current number). Start with state (0,0,0) and count all valid number till we reach number of steps equals to 10n.
This problem can also be solved using a dynamic programming approach and some knowledge of combinatorics.
Let f(k) = count of numbers with unique digits with length equals k.
f(1) = 10, ..., f(k) = 9 * 9 * 8 * ... (9 - k + 2) [The first factor is 9 because a number cannot start with 0].


### 分析：
This question is to get a count.
Given n, count the numbers which belong to [0, 10^n) and do not contain duplicate digits.

Firstly, this n must be less or equal to 10, since there are 0~9 10 unique digits.

When n=1, count=10. (0~9)
When n=2, there are 2 classes of numbers, one is 1-digit, another is 2-digit.
Under this n, when i==1, count=10.
when i==2, count=9*(8+1).
when i==3, count=9\*9\*(7+1)
...
when i==n, count=9\*9\*8..\*(9-n+2)

So here we can use Dynamic Programming.
Let dp[] to be an array with length=1*(n+1).
dp[k] means if a number is of k digits, how many kinds of combinations can satisfy the requirement.
For n, the number may have k=1~n situations.
For k, the choices on the (i)th position depends on the (i-1)th and before.
Finally, we will sum the dp from dp[0]~dp[n], and this is the result.

### Python

``` python
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
      
        n = min(n, 10)
        dp = [1] + [9]*n
        
        for k in xrange(2, n+1):
            for i in xrange(9, 9-k+1, -1):
                dp[k] *= i
        
        return sum(dp)
```
