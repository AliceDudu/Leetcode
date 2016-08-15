###题目：
https://leetcode.com/problems/shuffle-an-array/

>Shuffle a set of numbers without duplicates.

>Example:

>// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

>// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

>// Resets the array back to its original configuration [1,2,3].
solution.reset();

>// Returns the random shuffling of array [1,2,3].
solution.shuffle();


###题意：
Given an array and shuffle it randomly when calling 'shuffle' function, and return original array when calling 'reset'.


###分析：
For 'shuffle' function, use i to walk through the array from beginning to end, for each i, randomly pick up a number behind i, and swap it with num[i].

---

There are many applications of shuffle in real life, like [playing cards or listening to the music.](http://www.cnblogs.com/huaping-audio/archive/2008/09/09/1287985.html)

And basically there are 3 kinds of shuffle [algorithms.](http://www.cnblogs.com/tudas/p/3-shuffle-algorithm.html)
It depends on what kind of situation you want the array to be shuffled, you can shuffle the whole array every time, and you can also just pick up from the remaining numbers each time. You can build a new array to store the shuffle result, or you can rearrange the array in place.

You can have a look at the introduction about [Fisher–Yates shuffle algorithm.](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm)

And here is the [wonderful visualization of Fisher–Yates shuffle algorithm.](https://bost.ocks.org/mike/shuffle/)

For [more discussion.](http://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array)

---

###Python:

[random.randint(a, b)](https://docs.python.org/2/library/random.html)
Return a random integer N such that a <= N <= b.


``` python
import random
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.origin = nums[:]
        self.output = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        n = len(self.output)
        for i in range(n):
            j = random.randint(i,n-1)
            self.output[i], self.output[j] = self.output[j], self.output[i]
        return self.output
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
```


*Notice:*

self.origin = nums[:]


*Questions:*

- any improvement, challenge, follow-up ?
    1. To realize the randint yourself? 
    2. What if the array is very long? 
    3. How about each time just shuffle a window? 
    4. How about it can shuffle with a cycle without ending at the tail of origin array?
    5. If it's a short array and shuffle with cycle, can I know the past Nth number?
    
- what if the use of shuffle is more frequent than reset or vice versa
- what's the point for evaluation ?
