'''
Understand:
input: two binary trees p and q
output: boolean

plan:
consider same:
#1:root1:root2(val)
root1.left==root12.left 
root1.right == root2.right

repeating case
#root1.is None or root2 is None:
return False

#root1 and root2 is None

return checksame(root.left) or checksame(root.right)

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p:TreeNode, q:TreeNode) -> bool:
    #case1:
    if p is None and q is None:
        return True

    #case2:
    if p is None or q is None:
        return False
    
    #case3:

    if p.val != q.val:
        return False

    
    return (isSameTree(p.left,q.left)and isSameTree(p.right,q.right))


from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

tree1 = TreeNode(1, TreeNode(None), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
assert isSameTree(tree1, tree2) == True
print(isSameTree(tree1, tree2))




#Problem 1
"""

Understand: 

   Input: 
   
   Output: 
   
   Edge cases:

Match:


Plan: 

time complexity:
space complexity:

"""

