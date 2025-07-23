def is_circular(clues):
    if not clues:
        return False

    current = clues
    while current.next and current.next != clues:
        current = current.next

    return current.next == clues

def collect_false_evidence(evidence):
    def find_cycle_start(head):
        slow = fast = head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # No cycle

        # Step 2: Find start of cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # This is the cycle entry node

    # Main logic
    cycle_node = find_cycle_start(evidence)
    if not cycle_node:
        return []

    # Step 3: Traverse the cycle and collect values
    result = []
    current = cycle_node
    while True:
        result.append(current.value)
        current = current.next
        if current == cycle_node:
            break

    return result


def partition(suspect_ratings, threshold):
    greater_dummy = Node(0)
    less_equal_dummy = Node(0)

    greater_tail = greater_dummy
    less_equal_tail = less_equal_dummy

    current = suspect_ratings

    while current:
        next_node = current.next  # Save next pointer
        current.next = None       # Disconnect current node

        if current.value > threshold:
            greater_tail.next = current
            greater_tail = greater_tail.next
        else:
            less_equal_tail.next = current
            less_equal_tail = less_equal_tail.next

        current = next_node

    # Connect the two lists
    greater_tail.next = less_equal_dummy.next

    return greater_dummy.next


def merge_timelines(known_timeline, witness_timeline):
    dummy = Node(0)
    current = dummy

    while known_timeline and witness_timeline:
        if known_timeline.value <= witness_timeline.value:
            current.next = known_timeline
            known_timeline = known_timeline.next
        else:
            current.next = witness_timeline
            witness_timeline = witness_timeline.next
        current = current.next

    # Attach the rest of the non-empty list
    if known_timeline:
        current.next = known_timeline
    else:
        current.next = witness_timeline

    return dummy.next

def rotate_right(head, k):
    if not head or not head.next or k == 0:
        return head

    # Step 1: Find length and tail
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Normalize k
    k = k % length
    if k == 0:
        return head

    # Step 3: Connect tail to head (circular)
    tail.next = head

    # Step 4: Find new tail (length - k - 1 steps from head)
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    # Step 5: Break circle and set new head
    new_head = new_tail.next
    new_tail.next = None

    return new_head