# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
# 
# 
# 题意：
# 给个list，给个值，把list分为两部分，小于x的放在前，大于等于x的放在后，两部分各自保持原有顺序
# 
# 
# 思路：
# use p to move from head to end and compare each value with x
# create two dummy point, one is used to link points that are <x, another is to link points that are >=x



# Definition for singly-linked list.  
# class ListNode(object):  
#     def __init__(self, x):  
#         self.val = x  
#         self.next = None  
  
class Solution(object):  
    def partition(self, head, x):  
        """ 
        :type head: ListNode 
        :type x: int 
        :rtype: ListNode 
        """  
          
        if head is None or head.next is None or x is None:  
            return head  
          
        p1=head1=ListNode(0)  
        p2=head2=ListNode(0)  
        p=head  
          
        while p:  
            if p.val<x:  
                p1.next=p  
                p1=p1.next  
            else:  
                p2.next=p  
                p2=p2.next  
            p=p.next  
        p1.next=head2.next  
        p2.next=None  
        return head1.next  
