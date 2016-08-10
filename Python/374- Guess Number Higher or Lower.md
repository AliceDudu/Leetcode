题目：
https://leetcode.com/problems/guess-number-higher-or-lower/

>We are playing the Guess Game. The game is as follows:

>I pick a number from 1 to n. You have to guess which number I picked.

>Every time you guess wrong, I'll tell you whether the number is higher or lower.

>You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

>-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

>Return 6.


分析：

It's in the 'easy' class, given n, and return the number has been chosen among 1 to n, based on the feedback from the function called 'guess', we'll use 'Binary Search' to solve it.


``` python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left <= right:
            
            
            g = int((right+left)/2)
            
            if guess(g) == 1:
                left = g+1
                
            elif guess(g) == -1:
                right = g-1
            else:
                return g
                
        return left       

```
