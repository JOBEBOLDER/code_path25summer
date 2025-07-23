'''
understand:
-input:list:String(3 types)
- ouput:list

edge case:
 - empty list
 - random string
 - if 

plan:
schedule:
cancel:

for loop iterate the list
if string startwith schedule:
    get the last char 
    append schedule[a,c,b]
elif: cancel
    cancel:[]
    schedule.pop()
elif:reschedule:
    - get the top element from the cancel ,pop the element from the cancel
    - add it back to the schedule 
'''
def manage_stage_changes(changes):
    #base case:
    if not changes:
        return []
    
    #initialization
    schedule = []
    cancel = []

    # maintanance:
    for change in changes:
        if change.startswith('Schedule'):
            schedule.append(change[-1])

        elif change == 'Cancel':
            if schedule:
                cancel.append(schedule.pop())
            
        elif change == 'Reschedule':
            if cancel:
                schedule.append(cancel.pop())

    return schedule

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 


