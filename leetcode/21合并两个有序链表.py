"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""
class ListNode:
    def __init__(self, x, y):
        self.val = x
        self.next = y

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        visited = [] ## 建立缓存所有节点的列表
        while l1:
            visited.append(l1)
            l1 = l1.next
        while l2:
            visited.append(l2)
            l2 = l2.next
        print(visited)
        visited.sort(key=lambda x:x.val) ## 存完全部节点后，按节点val排序
        rst = None ## 新建结果节点，将列表节点存入此结果
        while visited:
            rst = ListNode(visited.pop().val,rst)  #循环依次将列表内的对象按小到大依次实例化
        print(rst)
        return rst



lis1 = ListNode(2,ListNode(3,None))
lis2 = ListNode(1,ListNode(4,None))
s = Solution()
new = s.mergeTwoLists(lis1,lis2)
print(new.__dict__)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = rst =ListNode(None) ## 新建节点和指针
        while True:
            try:
                while l1.val<=l2.val: ## 若l1更小，`p.next`就指向l1,同时更新l1，p节点
                    p.next = l1
                    l1, p = l1.next, p.next
                while l1.val>l2.val:  ## 若l2更小，`p.next`就指向l2,同时更新l2，p节点
                    p.next = l2
                    l2, p = l2.next, p.next
            except:break ## 发生异常时，一定l1/l2至少一个为None了
        p.next = l1 or l2 ## 接上不为None的节点
        return rst.next ##返回新建指针
