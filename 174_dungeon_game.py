# Dungeon Game
# Total Accepted: 8912 Total Submissions: 51778
# The demons had captured the princess (P) and imprisoned her
# in the bottom-right corner of a dungeon. The dungeon consists
# of M x N rooms laid out in a 2D grid. Our valiant knight (K)
# was initially positioned in the top-left room and must fight
# his way through the dungeon to rescue the princess.

# The knight has an initial health point represented by a positive
# integer. If at any point his health point drops to 0 or below ,
# he dies immediately.

# Some of the rooms are guarded by demons, so the knight loses health
# (negative integers) upon entering these rooms; other rooms are either
# empty (0's) or contain magic orbs that increase the knight's health
# (positive integers).

# In order to reach the princess as quickly as possible, the knight
# decides to move only rightward or downward in each step.


# Write a function to determine the knight's minimum initial health
# so that he is able to rescue the princess.

# For example, given the dungeon below, the initial health of the
# knight must be at least 7 if he follows the optimal path
# RIGHT-> RIGHT -> DOWN -> DOWN.

# -2(K)	-3	3
# -5	-10	1
# 10	30	-5 (P)

# Notes:

# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the
# knight enters and the bottom-right room where the princess is imprisoned.



# Keys:
# 1. This is a typical problem of Dynamic Programming:
#   - To find optimal path to (x, y), we need to find optimal paths to
#       (x, y-1), (x-1, y)
#       -> typical optimal substructure;
#   - Then compare the two, choose a better one to plus value at (x, y),
#     then remember this path to (x, y);
#   - Go on; 

def opt_path(inp):
    """ Mind we are tracing the prince's health along the way and
    guarding his life, not only waiting to see the final health.......

    *. Accumulate active health along each path with accu[][]
    *. Trace the lowest health along each path with low[][]
      -> Update the entry low[r][c] each time when accumulated
        health drops down under the lowest health so far. 
    *. Remember each path with path[][]
    """
    ROW = len(inp) ; COL = len(inp[0])
    # Allocation
    accu = [[None] * COL for _ in range(ROW)]
    low  = [[None] * COL for _ in range(ROW)]
    path = [[None] * COL for _ in range(ROW)]
    # Starting entry.
    accu[0][0] = inp[0][0]
    low[0][0]  = inp[0][0] 
    path[0][0] = 'START'
    # Boundary values.
    for c in range(1, COL):
        accu[0][c] = accu[0][c-1] + inp[0][c]
        path[0][c] = path[0][c-1] + ' RIGHT'
        low[0][c] = min(low[0][c-1], accu[0][c])
    for r in range(1, ROW):
        accu[r][0] = accu[r-1][0] + inp[r][0]
        path[r][0] = path[r-1][0] + ' DOWN'
        low[r][0] = min(low[r-1][0], accu[r][0])
    # Rest
    for r in range(1, ROW):
        for c in range(1, COL):
            if low[r][c-1] >= low[r-1][c]: # left-neighbor better than up-neighbor
                accu[r][c] = accu[r][c-1] + inp[r][c]
                low [r][c] = min(low[r][c-1], accu[r][c])
                path[r][c] = path[r][c-1] + ' RIGHT'
            else:
                accu[r][c] = accu[r-1][c] + inp[r][c]
                low [r][c] = min(low[r-1][c], accu[r][c])
                path[r][c] = path[r-1][c] + ' DOWN'
    return path[-1][-1] 

# Basic test:

inp = [
    [  -2,  -3,   3],
    [  -5, -10,   1],
    [  10,  30,  -5],
]
opt_path(inp)
# 'START RIGHT RIGHT DOWN DOWN'

inp1 = [
    [  -2,  -3,   3, -20],
    [  -5, -10,   1,   0],
    [  10,  30,  -5,   9],
]
opt_path(inp1)
# 'START RIGHT RIGHT DOWN RIGHT DOWN'
