def bidirectional_flights(flights):
    n = len(flights)  # Number of destinations

    # Iterate over each destination i
    for i in range(n):
        # Iterate over each destination j reachable from i
        for j in flights[i]:
            # Check if destination j has a flight back to i
            if i not in flights[j]:
                return False  # If not bidirectional, return False
    return True  # All flights are bidirectional, return True


def find_center(terminals):
    count = {}

    for u,v in terminals:
        count[u] = count.get(u,0) + 1
        count[v] = count.get(v,0) + 1

    
    for terminal,c in count.items():
        if c > 1:
            return terminal
        
    