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

def main():
	tree = Tree()
	for i in range(10):
		print(i)
		tree.add(i)

if __name__ == "__main__":
	main()

