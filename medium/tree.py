
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def printTree(self, opt):    	
    	"""    	    	
    	:type opt: str["pre", "in", "post"]    	
    	"""    	    	    	
    	nodes = treeToList(self, opt)
    	print(nodes)
    	    	

def createTree(nodes, i, j):
	if i > j:
		return None
            
	mid = (i + j) // 2
	root = TreeNode(nodes[mid])
	root.left = createTree(nodes, i, mid - 1)
	root.right = createTree(nodes, mid  + 1, j)

	return root
	
	
def treeToList(root, opt):
  """
  :type opt: str["pre", "in", "post"]
  :rtype nodes: List[int]
  """
  nodes = []    	    	    	
  def preTraversal(node):
   	if node:    			
   		preTraversal(node.left)
   		nodes.append(node.val)    			
   		preTraversal(node.right)
   	
  def inTraversal(node):
  	if node:    			    			
   		nodes.append(node.val)    			
   		inTraversal(node.left)
   		inTraversal(node.right)
   		
  def postTraversal(node):
   	if node:    			
   		postTraversal(node.right)    			
   		nodes.append(node.val)  
   		postTraversal(node.left)  			    			
    	
  if opt == "pre":
  		preTraversal(root)
  elif opt == "in":
  		inTraversal(root)
  elif opt == "post":
  		postTraversal(root)
  else:
   		pass
    	
  return nodes   