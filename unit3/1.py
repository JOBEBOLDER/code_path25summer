#question1
'''
input:lists
output:lists
do,undo feature

plan:
two stack:
schedule:[A,C,B,D]
cancel:[b]
#Another stack (canceled) to remember what was recently removed, so we can bring it back if needed.”

-create 2 stacks:
- we are going to traverse the "changes" list
    - schedule X:
        put the X in the schedule stack
        move to the next one element
    - Cancel
        -put previous X to cancel stack
        - pop the previous X from the schedule stack
        - move to the next one

    - Reschedule
        - get the top element from the cancel stack and add it back to the schedule stack
        - move to the next one

return the schedule stack

'''
def manage_stage_changes(changes):
    #initialization:
    schedule =[]
    cancel = []

    for change in changes:
        if change.startswith('Schedule'):
            performance_id = change.split()[-1]
            schedule.append(performance_id)
        elif 'Cancel' in change:
            if schedule:
                cancel_id = schedule.pop()
                cancel.append(cancel_id)
        elif 'Reschedule' in change:
            if cancel:
                schedule.append(cancel.pop())
    return schedule

        
print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 


#question2
def process_performance_requests(requests):
    if requests:
        requests.sort(key=lambda x:x[0],reverse=True)
    result = []
    for perfomance_name in requests:
        result.append(perfomance_name[1])
    return result
print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))


#question3
def collect_festival_points(points):
    #return sum(points)
    stack = []
    for point in points:
        stack.append(point)
    return sum(stack)
print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 

def booth_navigation(clues):
    do = []

    for clue in clues:
        if clue != 'back':
            do.append(clue)
        elif clue == 'back':
            if do:
                do.pop()

    return do

clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues)) 

#two pointer
def merge_schedules(schedule1, schedule2):
    list1 = list(schedule1)
    list2 = list(schedule2)
    start1 = 0
    start2 = 0
    result = []

    while start1 < len(list1) and start2 < len(list2):
        result.append(list1[start1])
        start1 += 1
        result.append(list2[start2])
        start2 += 1
    if list1:
        result.extend(list1[start1:])
    if list2:
        result.extend(list2[start2:])
    return "".join(result)

print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq")) 

def nextGreaterElement(nums1, nums2):
        next_greater = {}
        stack = []

        for num in nums2:
            if stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        for num2 in stack:
            next_greater[num] = -1


        result = []
        for element in nums1:
            if element in next_greater:
                result.append(next_greater[element])
        return result
print(nextGreaterElement(nums1=[4,1,2],nums2=[1,3,4,2]))

#