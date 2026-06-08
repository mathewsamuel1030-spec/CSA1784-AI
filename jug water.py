from collections import deque

# BFS function for Water Jug Problem
def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        # Check goal state
        if x == target or y == target:
            return path

        # Generate successor states
        next_states = [
            (jug1, y),                    # Fill Jug 1
            (x, jug2),                    # Fill Jug 2
            (0, y),                       # Empty Jug 1
            (x, 0),                       # Empty Jug 2
            (max(0, x - (jug2 - y)),
             min(jug2, y + x)),           # Pour Jug 1 -> Jug 2
            (min(jug1, x + y),
             max(0, y - (jug1 - x)))      # Pour Jug 2 -> Jug 1
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

    return None

# Example
jug1_capacity = 4
jug2_capacity = 3
target = 2

solution = water_jug_bfs(jug1_capacity, jug2_capacity, target)

if solution:
    print("Steps to reach the target:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
