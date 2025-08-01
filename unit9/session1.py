class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right
from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

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



def merge_orders(order1, order2):
    return buildhelper(order1,order2)

def buildhelper(root1,root2):

    if root1 is None and root2 is None:
        return None
    
    if root1 is None:
        return root2
    
    if root2 is None:
        return root1
    
    root = TreeNode(root1.val + root2.val)

    root.left = buildhelper(root1.left, root2.left)
    root.right = buildhelper(root1.right,root2.right)

    return root

# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    #bfs
    #base case :
    if design is None:
        return None
    
    queue = deque([design])

    result = []

    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            result.append(cur.val)

            if cur.left:
                queue.append(cur.left)

            if cur.right:
                queue.append(cur.right)

    return result

"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print(print_design(croquembouche))


class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    #base case
    if not cake:
        return 0
    
    queue = deque([cake])
    layer = 0

    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        layer += 1# 一层处理完了才加1

    return layer 
        
            
"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))


def max_tiers(cake):
    if not cake:
        return 0
    
    left_depth = max_tiers(cake.left)
    right_depth = max_tiers(cake.right)

    return max(left_depth,right_depth) + 1

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))

#to check if there is a path that the root.val sum up can == order_size
class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def can_fulfill_order(inventory, order_size):
    #base case:
    if not inventory:
        return False
    return traverse(inventory,order_size,0)
    
def traverse(root,target,cur_sum):
    if not root:
        return False
    cur_sum += root.val
    
    #only check if we reach the leaf node
    if not root.left and not root.right:
        if cur_sum == target:
            return True
        else:
            return False
        
    return traverse(root.left,target,cur_sum) or traverse(root.right,target,cur_sum)
    
    
"""
             5
           /   \
          4     8
        /      /  \
       11     13   4
      /  \          \
     7   2           1   
"""

# Using build_tree() function included at top of the page
quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)

print(can_fulfill_order(baked_goods, 22))
print(can_fulfill_order(baked_goods, 2))


class TreeNode():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def zigzag_icing_order(cupcakes):
    #base case:
    if not cupcakes:
        return None
    
    result = []
    result.append(cupcakes)

    queue = deque([cupcakes])
    flag = True
    while queue:
        level=[]
        for _ in range(len(queue)):
            cur = queue.popleft()
            level.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        if not flag:
            level.reverse()

    #     	•	把这一层的最终顺序添加进结果 result 中。
	# •	然后把方向反转一下，保证下一层走相反的方向（从左→右 或 从右→左）。
        result.extend(level)
        flag = False
    return result
            
"""
            Chocolate
           /         \
        Vanilla       Lemon
       /              /    \
    Strawberry   Hazelnut   Red Velvet   
"""

# Using build_tree() function included at top of page
flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
print(zigzag_icing_order(cupcakes))

