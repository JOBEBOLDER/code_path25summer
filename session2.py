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
         
def count_odd_splits(root):
    return count_odd_helper(root)
    
def count_odd_helper(node):
    if not node:
        return 0
    
    count = 1 if node.val % 2 == 1 else 0
    count += count_odd_helper(node.left)
    count += count_odd_helper(node.right)
    return count

"""
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12
"""

# Using build_tree() function included at top of page
# #	•	Recursive call stack: O(h) where h is the height of the tree
# 	•	In balanced tree: O(log n)
# 	•	In worst case (skewed): O(n)

values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))

def find_flower(inventory, name):
    if not inventory:
        return False
    
    if inventory.val == name:
        return True
    elif inventory.val < name:
        return find_flower(inventory.right, name)
    else:
        return find_flower(inventory.left,name)

"""
          Rose
         /    \
      Lilac  Tulip
      /  \       \
   Daisy Lily   Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower"))

#problem 3:
'''
1. The key difference is that `find_flower()` uses the BST property to guide the search,
so it only explores one side (left or right) based on comparison. This saves time.

In contrast, `non_bst_find_flower()` has no ordering, so it must recursively check both
left and right subtrees until it finds a match, meaning it may visit all nodes.

2. The time complexity of `non_bst_find_flower()` is O(n) in the worst case, 
since it may need to visit every node in the tree.

3. If the inventory tree in `find_flower()` is not balanced, the search path could be 
as long as the number of nodes, making the worst-case time complexity also O(n),
same as `non_bst_find_flower()`.

'''
def add_plant(collection, name):
    if not collection:
        return TreeNode(name)
    
    if name < collection.val:
        collection.left = add_plant(collection.left, name)
    else:
        collection.right = add_plant(collection.right,name)

    return collection
    
"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))
