import heapq

# Goal State
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Manhattan Distance Heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = goal_state.index(state[i])
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_pos, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Generate Successor States
def get_neighbors(state):
    neighbors = []
    zero_pos = state.index(0)

    moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7]
    }

    for move in moves[zero_pos]:
        new_state = list(state)
        new_state[zero_pos], new_state[move] = (
            new_state[move],
            new_state[zero_pos],
        )
        neighbors.append(tuple(new_state))

    return neighbors

# A* Search Algorithm
def a_star(start_state):
    frontier = []
    heapq.heappush(frontier, (manhattan_distance(start_state), 0, start_state))

    visited = set()

    while frontier:
        f, g, current = heapq.heappop(frontier)

        if current == goal_state:
            return True

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + manhattan_distance(neighbor)
                heapq.heappush(frontier, (new_f, new_g, neighbor))

    return False

# Example Start State
start_state = (1, 2, 3,
               4, 0, 6,
               7, 5, 8)

# Solve Puzzle
if a_star(start_state):
    print("Goal State Reached!")
else:
    print("No Solution Found.")
