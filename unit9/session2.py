class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

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


class Solution:
    def __init__(self):
        self.balanced = True  # 默认认为树是平衡的

    def is_balanced(self, root) -> bool:
        self.getHeight(root)
        return self.balanced

    def getHeight(self, root):
        # base case: 空节点高度为 0
        if root is None:
            return 0

        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        # 如果左右子树高度差大于 1，标记为不平衡
        if abs(left - right) > 1:
            self.balanced = False

        # 当前节点高度 = max(左右子树高度) + 1
        return 1 + max(left, right)


# Using build_tree() function included at top of page
baked_goods = ["🎂", "🥮", "🍩", "🥖", "🧁"]
display1 = build_tree(baked_goods)


baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)

sol = Solution()

print(sol.is_balanced(display1)) 
print(sol.is_balanced(display2)) 


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_each_days_orders(orders):
	#level order traversal:
    queue = deque([orders])
    #collect the result
    result = []
    while queue:
        cur_sum = 0
        for _ in range(len(queue)):
            curval = queue.popleft()
            cur_sum += curval.val

            if curval.left:
                queue.append(curval.left)

            if curval.right:
                queue.append(curval.right)
        result.append(cur_sum)
    return result

"""
      4
     / \
    2   6
   / \  
  1   3
"""

# Using build_tree() function included at top of page
order_sizes = [4, 2, 6, 1, 3]
orders = build_tree(order_sizes)

print(sum_each_days_orders(orders))


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sweet_difference(chocolates):
	#level order traversal:
    queue = deque([chocolates])
    #collect the result
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        if len(queue) == 1:
            result.append(0)
        else:
            result.append(max(level)-min(level))
        
    return result

"""
  3
 / \
9  20
   / \
  15  7
"""
# Using build_tree() function included at top of page
sweetness_levels1 = [3, 9, 20, None, None, 15, 7]
chocolate_box1 = build_tree(sweetness_levels1)

"""
    1
   / \
  2   3
 / \   \
4   5   6

"""
sweetness_levels2 = [1, 2, 3, 4, 5, None, 6]
chocolate_box2 = build_tree(sweetness_levels2)

print(sweet_difference(chocolate_box1))  
print(sweet_difference(chocolate_box2)) 


def can_rearrange_orders(order1, order2):
    if not order1 and not order2:
        return True
    if not order1 or not order2:
        return False
    if order1.val != order2.val:
        return False

    # 不交换的情况
    no_swap = can_rearrange_orders(order1.left, order2.left) and \
              can_rearrange_orders(order1.right, order2.right)

    # 交换左右子树
    swap = can_rearrange_orders(order1.left, order2.right) and \
           can_rearrange_orders(order1.right, order2.left)

    return no_swap or swap