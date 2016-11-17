#coding=utf-8

class Node(object):
	"""节点类"""
	def __init__(self,elem=-1,lchild=None,rchild=None):
		self.elem = elem
		self.lchild = lchild
		self.rchild = rchild

class Tree(object):
	"""树类"""
	def __init__(self):
		self.root = Node()
		self.dataList = []
	def add(self,elem):
		"""为树增加节点"""
		node = Node(elem)
		#判断根节点是否为空
		if self.root.elem == -1:
			self.root = node
		else:
			treeNode = self.root
			treeQueue = []
			treeQueue.append(treeNode)
			#对节点进行遍历
			while treeQueue:
				#取出队列第一个元素
				temp = treeQueue.pop(0)
				if temp.lchild == None:
					temp.lchild = node
					return
				elif temp.rchild == None:
					temp.rchild = node
					return
				else:
					#如果本节点左右子节点均存在,加入队列,开始下次遍历
					treeQueue.append(temp.lchild)
					treeQueue.append(temp.rchild)
	
	def front(self):
		"""深度优先遍历之先序遍历"""
		self.front_f(self.root)
	
	def front_f(self,root):
		"""先序遍历之嵌套"""
		if root==None:
			return
		self.dataList.append(root.elem)
		self.front_f(root.lchild)
		self.front_f(root.rchild)

	def middle(self):
		"""深度优先遍历之中序遍历"""
		self.middle_m(self.root)
	
	def middle_m(self,root):
		"""中序遍历之嵌套"""
		if root == None:
			return
		self.middle_m(root.lchild)
		self.dataList.append(root.elem)
		self.middle_m(root.rchild)

	def last(self):
		"""深度优先遍历之后序遍历"""
		self.last_l(self.root)

	def last_l(self, root):
		"""后序遍历之嵌套"""
		if root == None:
			return 
		self.last_l(root.lchild)
		self.last_l(root.rchild)
		self.dataList.append(root.elem)

	def levelQueue(self):
		"""广度优先遍历之层次遍历"""
		if self.root == None:
			return
		treeQueue = []
		treeQueue.append(self.root)
		while(treeQueue):
			temp = treeQueue.pop(0)
			self.dataList.append(temp.elem)
			if temp.lchild != None:
				treeQueue.append(temp.lchild)
			if temp.rchild != None:
				treeQueue.append(temp.rchild)

def main():
	tree = Tree()
	for i in range(10):
		tree.add(i)
	# tree.front()
	# tree.middle()
	# tree.last()
	tree.levelQueue()
	print tree.dataList

if __name__ == "__main__":
	main()

