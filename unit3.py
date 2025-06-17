def is_valid_post_format(posts):
    stack = []

    for s in posts:
        if s == '(':
            stack.append(')')
        elif s == '[':
            stack.append(']')
        elif s == '{':
            stack.append('}')

        else:
            if not stack or s != stack[-1]:
                return False
            stack.pop()
    
    return not stack

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))


def reverse_comments_queue(comments):
    #return comments[::-1]
    stack = []
    reversed_stack = []
    for comment in comments:
        stack.append(comment)
    while stack:
        reversed_stack.append(stack.pop())

    return reversed_stack

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

def is_symmetrical_title(title):
    no_space = title.replace(" ","")

    title_list = list(no_space)
    print(title_list)

    left = 0
    right = len(title_list) - 1
    while left < right:
        if title_list[left].upper() != title_list[right].upper():
            return False
        left += 1
        right -= 1

    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 



def engagement_boost(engagements):
    result = [0] * len(engagements)
    left = 0
    right = len(engagements) - 1
    position = len(engagements) - 1

    while left <= right:
        left_sq = engagements[left] ** 2
        right_sq = engagements[right] ** 2

        if left_sq > right_sq:
            result[position] = left_sq
            left += 1
        else:
            result[position] = right_sq
            right -= 1

        position -= 1

    return result

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

def clean_post(post):
    stack = []
    for p in post:
        if stack and p.upper() == stack[-1].upper():
            stack.pop()
        stack.append(p)
    result = []
    while stack:
        result.append(stack.pop())
    return "".join(result[::-1])
print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 