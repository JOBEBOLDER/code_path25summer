#problem 1
# unit1.py
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# Level 3
fuji = TreeNode("Fuji")
opal = TreeNode("Opal")
crab = TreeNode("Crab")
gala = TreeNode("Gala")

# Level 2
mcintosh = TreeNode("McIntosh", left=fuji, right=opal)
granny_smith = TreeNode("Granny Smith", left=crab, right=gala)

# Level 1 (Root)
root = TreeNode("Trunk", left=mcintosh, right=granny_smith)

def print_tree(node):
    if not node:
        return []
    return [node.val] + print_tree(node.left) + print_tree(node.right)

print(print_tree(root))


#problem 2:
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
  if not root:
      return 0
  
  cur_val = 0
  
  if root.val == '+':
      cur_val = root.left.val + root.right.val
  elif root.val == '-':
      cur_val = root.left.val - root.right.val
  elif root.val == '*':
      cur_val = root.left.val * root.right.val
  elif root.val == '/':
      cur_val = root.left.val / root.right.val
  return cur_val
  
"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
apple_tree2 = TreeNode("-", TreeNode(7), TreeNode(5))
apple_tree3 = TreeNode("*", TreeNode(7), TreeNode(5))
apple_tree4 = TreeNode("/", TreeNode(7), TreeNode(5))

print(calculate_yield(apple_tree))
print(calculate_yield(apple_tree2))
print(calculate_yield(apple_tree3))
print(calculate_yield(apple_tree4))

#time:Oh
#space:On
#iterative method
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
  if not root:
      return None
  result = []

  current = root
  while current:
      result.append(current.val)
      current = current.right
  return result
      
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))


def right_vine(root):
    if not root:
        return []
    #every time get the result you need to return so that you can use it next time
    return [root.val] + right_vine(root.right)

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
#Each node is visited once → O(n) where n is the number of nodes.
def count_leaves(root):
    count = 0
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


print(count_leaves(oak1))
print(count_leaves(oak2))

#postorder traversal:
#left-right-root
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    if not root:
        return []
    
    #explore all the left tree node
    left = survey_tree(root.left)
    #explore all the right tree node
    right = survey_tree(root.right)
    return left + right + [root.val]
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def harvest_berries(root, threshold):
    if not root:
        return 0

    left_sum = harvest_berries(root.left, threshold)
    right_sum = harvest_berries(root.right, threshold)
    current = root.val if root.val > threshold else 0

    return current + left_sum + right_sum

"""
       4
     /   \
   10     6
  /  \     \
 5    8    20
"""
bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

print(harvest_berries(bush, 6))
print(harvest_berries(bush, 30))

def find_flower(root, flower):
    if not root:
        return False
    
    if root.val == flower:
        return True
    
    return find_flower(root.left, flower) or find_flower(root.right, flower)

"""
         Rose
        /    \
       /      \
     Lily     Daisy
    /    \        \
Orchid  Lilac    Dahlia
"""

flower_field = TreeNode("Rose", 
                        TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                                TreeNode("Daisy", None, TreeNode("Dahlia")))

print(find_flower(flower_field, "Lilac"))
print(find_flower(flower_field, "Hibiscus"))