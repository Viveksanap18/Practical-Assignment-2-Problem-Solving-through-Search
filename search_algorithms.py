import time
import heapq
from collections import deque

# Campus graph (directed, distances in metres)
graph = {
    "Parking Area": {"Workshop": 90, "Canteen": 70, "Sports Complex": 120},
    "Workshop": {"Computer Center": 60},
    "Canteen": {"Hostel Block": 50, "Placement Cell": 110},
    "Sports Complex": {"Admin Office": 40},
    "Computer Center": {"Library": 40},
    "Hostel Block": {"Auditorium": 190},
    "Placement Cell": {"Auditorium": 60},
    "Admin Office": {"Auditorium": 90},
    "Library": {"Auditorium": 80},
    "Auditorium": {},
}

# Heuristic: estimated remaining distance to the Auditorium (metres)
h = {
    "Parking Area": 200,
    "Workshop": 170,
    "Canteen": 150,
    "Sports Complex": 100,
    "Computer Center": 110,
    "Hostel Block": 170,
    "Placement Cell": 60,
    "Admin Office": 90,
    "Library": 70,
    "Auditorium": 0,
}

START = "Parking Area"
GOAL = "Auditorium"


def bfs(start, goal):
    queue = deque([(start, [start], 0)])
    visited = set()
    nodes = 0
    while queue:
        current, path, cost = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        nodes += 1
        if current == goal:
            return path, cost, nodes
        for nxt, dist in graph[current].items():
            if nxt not in visited:
                queue.append((nxt, path + [nxt], cost + dist))
    return None, 0, nodes


def dfs(start, goal):
    stack = [(start, [start], 0)]
    visited = set()
    nodes = 0
    while stack:
        current, path, cost = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        nodes += 1
        if current == goal:
            return path, cost, nodes
        for nxt, dist in reversed(list(graph[current].items())):
            if nxt not in visited:
                stack.append((nxt, path + [nxt], cost + dist))
    return None, 0, nodes


def greedy(start, goal):
    frontier = [(h[start], start, [start], 0)]
    visited = set()
    nodes = 0
    while frontier:
        _, current, path, cost = heapq.heappop(frontier)
        if current in visited:
            continue
        visited.add(current)
        nodes += 1
        if current == goal:
            return path, cost, nodes
        for nxt, dist in graph[current].items():
            if nxt not in visited:
                heapq.heappush(frontier, (h[nxt], nxt, path + [nxt], cost + dist))
    return None, 0, nodes


def a_star(start, goal):
    pq = [(h[start], 0, start, [start])]
    best_cost = {start: 0}
    nodes = 0
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if g > best_cost.get(current, float("inf")):
            continue
        nodes += 1
        if current == goal:
            return path, g, nodes
        for nxt, dist in graph[current].items():
            new_g = g + dist
            if nxt not in best_cost or new_g < best_cost[nxt]:
                best_cost[nxt] = new_g
                heapq.heappush(pq, (new_g + h[nxt], new_g, nxt, path + [nxt]))
    return None, 0, nodes


def hill_climbing(start, goal):
    current, path, cost, nodes = start, [start], 0, 0
    while current != goal:
        nodes += 1
        neighbours = list(graph[current].items())
        if not neighbours:
            return None, cost, nodes
        nxt, dist = min(neighbours, key=lambda item: h[item[0]])
        if h[nxt] >= h[current]:
            return None, cost, nodes
        cost += dist
        current = nxt
        path.append(current)
    nodes += 1
    return path, cost, nodes


def solve_n_queens(n):
    board = [-1] * n
    nodes = 0

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        nonlocal nodes
        nodes += 1
        if row == n:
            return True
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                if backtrack(row + 1):
                    return True
                board[row] = -1
        return False

    t0 = time.perf_counter()
    solved = backtrack(0)
    t1 = time.perf_counter()
    return solved, board, nodes, t1 - t0


def test_algorithm(name, function):
    t0 = time.perf_counter()
    path, cost, nodes = function(START, GOAL)
    t1 = time.perf_counter()
    print("\n" + "=" * 55)
    print("Algorithm:", name)
    print("=" * 55)
    if path:
        print("Path:", " -> ".join(path))
        print("Total Distance:", cost, "m")
    else:
        print("No solution found")
    print("Nodes Explored:", nodes)
    print("Execution Time:", f"{t1 - t0:.6f}", "seconds")


print("=" * 60)
print("CAMPUS NAVIGATION - SEARCH ALGORITHM EVALUATION")
print("=" * 60)
test_algorithm("Breadth First Search", bfs)
test_algorithm("Depth First Search", dfs)
test_algorithm("Greedy Best-First Search", greedy)
test_algorithm("A* Search", a_star)
test_algorithm("Hill Climbing", hill_climbing)

print("\n" + "=" * 60)
print("CONSTRAINT SATISFACTION - N QUEENS")
print("=" * 60)
n = 6
solved, board, nodes, execution_time = solve_n_queens(n)
if solved:
    print("N =", n)
    print("Solution:", board)
    print("Nodes Explored:", nodes)
    print("Execution Time:", f"{execution_time:.6f}", "seconds")
else:
    print("No solution found")
