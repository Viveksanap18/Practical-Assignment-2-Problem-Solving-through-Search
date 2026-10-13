# Practical 2 – Problem Solving through Search

**TY B.Tech. – Artificial Intelligence and Machine Learning**

| | |
|---|---|
| **Student Name** | Vivek Vilas Sanap |
| **PRN** | 202401040091 |
| **Division / Roll No.** | B / 91 |
| **Faculty** | Dr. Khushal Khairnar |
| **Practical Title** | Problem Solving through Search |

---

## Problem Statement

A **College Campus Navigation Problem**: find a route from the **Parking Area** (start) to the **Auditorium** (goal) on a campus graph, using different search techniques, and compare them on route distance, nodes explored, execution time and optimality.

Techniques covered:

- **Uninformed Search:** Breadth First Search (BFS), Depth First Search (DFS)
- **Informed Search:** Greedy Best-First Search, A* Search
- **Local Search:** Hill Climbing
- **Constraint Satisfaction:** N-Queens using Backtracking

## Campus Graph

Distances are one-way road lengths in metres.

| From | To | Distance |
|---|---|---|
| Parking Area | Workshop | 90 m |
| Parking Area | Canteen | 70 m |
| Parking Area | Sports Complex | 120 m |
| Workshop | Computer Center | 60 m |
| Canteen | Hostel Block | 50 m |
| Canteen | Placement Cell | 110 m |
| Sports Complex | Admin Office | 40 m |
| Computer Center | Library | 40 m |
| Hostel Block | Auditorium | 190 m |
| Placement Cell | Auditorium | 60 m |
| Admin Office | Auditorium | 90 m |
| Library | Auditorium | 80 m |

**Heuristic h(n)** – estimated remaining distance to the Auditorium (admissible):

| Location | h(n) | Location | h(n) |
|---|---|---|---|
| Parking Area | 200 | Hostel Block | 170 |
| Workshop | 170 | Placement Cell | 60 |
| Canteen | 150 | Admin Office | 90 |
| Sports Complex | 100 | Library | 70 |
| Computer Center | 110 | Auditorium | 0 |

## Requirements

- Python 3.8 or higher
- No external libraries. Only the standard library is used: `time`, `heapq`, `collections.deque`

## How to Run

```bash
python search_algorithms.py
```

It can also be pasted into a Jupyter Notebook cell and run.

## Results

| Algorithm | Search Type | Route | Cost | Nodes Explored | Optimal |
|---|---|---|---|---|---|
| BFS | Uninformed | Parking Area → Canteen → Hostel Block → Auditorium | 310 m | 10 | No |
| DFS | Uninformed | Parking Area → Workshop → Computer Center → Library → Auditorium | 270 m | 5 | No |
| Greedy Best-First | Informed | Parking Area → Sports Complex → Admin Office → Auditorium | 250 m | 4 | No |
| A* | Informed | Parking Area → Canteen → Placement Cell → Auditorium | **240 m** | 5 | **Yes** |
| Hill Climbing | Local Search | Parking Area → Sports Complex → Admin Office → Auditorium | 250 m | 4 | No |
| N-Queens (N = 6) | CSP | Solution: `[1, 3, 5, 0, 2, 4]` | – | 32 | – |

Execution times are in the order of microseconds for this small graph and vary slightly from run to run.

**Optimal route:** Parking Area → Canteen → Placement Cell → Auditorium = 70 + 110 + 60 = **240 m**

## Key Observations

- **BFS** finds a route with the fewest edges but ignores distance, so it is not guaranteed to be the cheapest.
- **DFS** goes deep along the first branch; it used the fewest nodes among the uninformed methods here but gives no cost guarantee.
- **Greedy Best-First** uses only h(n) and was pulled toward the Sports Complex, giving 250 m (10 m above optimal).
- **A\*** uses f(n) = g(n) + h(n) and, because h(n) is admissible, returns the optimal 240 m route.
- **Hill Climbing** moves to the best neighbour only and never backtracks; it reached the goal here but can stop at a local optimum.
- **N-Queens** backtracking undoes a placement as soon as a column or diagonal conflict appears.

## Project Structure

```
.
├── search_algorithms.py   # All algorithms + test driver
├── README.md              # This file
└── Practical-Assignment-2.pdf   # Submitted practical report
```

## Algorithm Summary

| Algorithm | Data Structure | Evaluation |
|---|---|---|
| BFS | Queue (`deque`) | Level order |
| DFS | Stack (list) | Deepest first |
| Greedy Best-First | Priority queue (`heapq`) | f(n) = h(n) |
| A* | Priority queue (`heapq`) | f(n) = g(n) + h(n) |
| Hill Climbing | Current state only | Best neighbouring h(n) |
| N-Queens | Recursion (backtracking) | Column and diagonal constraints |
