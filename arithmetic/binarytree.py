# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Date: 2021-02-08 17:46:13
LastEditTime: 2021-02-08 17:46:38
"""

"""完全二叉树结构及其四种遍历实现"""


class Node(object):
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""

    def __init__(self):
        self.root = Node()
        self.data_list = []

    def add(self, elem):
        """为树增加节点"""
        node = Node(elem)
        # 判断根节点是否为空
        if self.root.elem == -1:
            self.root = node
        else:
            tree_node = self.root
            tree_queue = []
            tree_queue.append(tree_node)
            # 对节点进行遍历
            while tree_queue:
                # 取出队列第一个元素
                temp = tree_queue.pop(0)
                if temp.lchild is None:
                    temp.lchild = node
                    return
                elif temp.rchild is None:
                    temp.rchild = node
                    return
                else:
                    # 如果本节点左右子节点均存在,加入队列,开始下次遍历
                    tree_queue.append(temp.lchild)
                    tree_queue.append(temp.rchild)

    def front(self):
        """深度优先遍历之先序遍历"""
        self.front_f(self.root)

    def front_f(self, root):
        """先序遍历之嵌套"""
        if root is None:
            return
        self.data_list.append(root.elem)
        self.front_f(root.lchild)
        self.front_f(root.rchild)

    def middle(self):
        """深度优先遍历之中序遍历"""
        self.middle_m(self.root)

    def middle_m(self, root):
        """中序遍历之嵌套"""
        if root is None:
            return
        self.middle_m(root.lchild)
        self.data_list.append(root.elem)
        self.middle_m(root.rchild)

    def last(self):
        """深度优先遍历之后序遍历"""
        self.last_l(self.root)

    def last_l(self, root):
        """后序遍历之嵌套"""
        if root is None:
            return
        self.last_l(root.lchild)
        self.last_l(root.rchild)
        self.data_list.append(root.elem)

    def level_queue(self):
        """广度优先遍历之层次遍历"""
        if self.root is None:
            return
        tree_queue = []
        tree_queue.append(self.root)
        while tree_queue:
            temp = tree_queue.pop(0)
            self.data_list.append(temp.elem)
            if temp.lchild is not None:
                tree_queue.append(temp.lchild)
            if temp.rchild is not None:
                tree_queue.append(temp.rchild)


def main():
    tree = Tree()
    lists = list(range(10))
    for i in lists:
        tree.add(i)
    print(lists)
    print(tree.data_list)
    tree.front()
    print(tree.data_list)
    tree.middle()
    print(tree.data_list)
    tree.last()
    print(tree.data_list)
    tree.level_queue()
    print(tree.data_list)


if __name__ == "__main__":
    main()
