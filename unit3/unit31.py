#quesiton1
'''
understand:
-input: string:() for mentions, [] for hashtags, and {} for links
-output:boolean 

-edge case:
1.empty posts
2.[{}]

plan:
- DS: stack
"( )[] { }"
   ^
[ ]
time: On
space:On

1. create a empty stack -> store the processing elements

2.loop over the string:posts
    2.1 if we find a closing tag: return Flase
    2.2: if we find a opening tag:
        '[', '(','{'
        put the closing tag to the stack
        compare the last element from the stack if they are the same then we can pop it
'''
def is_valid_post_format(posts):
    #base case:
    if not posts:
        return False
    
    stack = []
    
    #do the for loop:
    for post in posts:
        if post == '(':
            stack.append(')')
        elif post == '[':
            stack.append(']')
        elif post == '{':
            stack.append('}')
        else:
            if stack and post != stack[-1]:
                return False
            else:
                stack.pop()
        print(stack)
    return False if stack else True


print(is_valid_post_format("()[]{}("))
print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
        
#below method that save the memory when there are some cases like:(((((((((((((((((())))))))))))))))
def is_valid_post_format(post):
    stack = []
    matching_tags = {')': '(', ']': '[', '}': '{'}

    for char in post:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != matching_tags[char]:
                return False

    return len(stack) == 0