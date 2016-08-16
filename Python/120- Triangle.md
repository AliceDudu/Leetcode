####题目：
https://leetcode.com/problems/triangle/

>Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

>For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

>Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


####题意：
Given a triangle, and this problem is to find the minimum sum from top to down layer, at each layer, for each point, it can only sum with its adjacent point.


####分析：

Since that when we move to the next layer, the sum depends on the previous layer's choice, and each choice maybe called more than once, so it's better to use Dynamic Programming to deal with it.

If we solve it from top to down, it may require to build 2D matrix.
So we can try from down to top.

- Suppose the triangle has n layers.

- We firstly initiate dp as equal to the last layer of triangle, so dp has 1*n dimension.

- Then we move from (n-1)th layer upward, for each movement, we will compare and store the minimum choice for each point in this layer. That is:

- At (n-1)th layer, for each i in this layer, find min(triangle[i]+dp[i], triangle[i]+dp[i+1]), then refresh dp[i] with the result.

- So dp[i] denote that, till current time, when we move from down to current layer, the minimum so far for each point i in this layer.


![图例](http://img.blog.csdn.net/20160816232845798)

####［Python］
``` python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        n = len(triangle)
        
        dp = triangle[n-1]
        
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                dp[j] = min( dp[j], dp[j+1] ) + triangle[i][j]
        
        return dp[0]

```


