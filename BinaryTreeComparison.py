import collections
#This solution was mapped out online in pseudo-code by w3 schools. 
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def identicalTrees(p,q): # This would be a helper function for doing BFS and DFS on deeper trees

	if p == None and q == None:
		return True
	if p == None and q != None:
		return False
	if q == None and p != None:
		return False

	if p != None and q != None:
		if p.val != None and q.val != None:
			return (q.val == p.val) and (identicalTrees(p.left, q.left)) and (identicalTrees(p.right, q.right))












#Tree one nodes:[1, TreeNode{val: 2, left: None, right: None}, TreeNode{val: 3, left: None, right: None}]
#Tree two nodes:[1, TreeNode{val: 2, left: None, right: None}, TreeNode{val: 3, left: None, right: None}]
#Both arrays are DIFF returning false


# Define some test trees
first_tree = TreeNode(1,None, TreeNode(2, None, TreeNode(3, None, None)))


second_tree = TreeNode(1,None, TreeNode(2, None, TreeNode(3, None, None)))




third_tree = TreeNode(2,TreeNode(4, None, None), )




a = identicalTrees(first_tree, second_tree) 
print(a)

