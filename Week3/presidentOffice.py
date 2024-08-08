# Importing necessary libraries
import sys
import math
from collections import deque
from typing import Set

# Function to check if the coordinates are valid
def valid(x, y):
    return 0 <= x < n and 0 <= y < m

# Directions arrays to check the neighboring cells
dirx = [-1, 0, 1, 0]
diry = [0, 1, 0, -1]

# Read input values
n, m, col = map(str, input().split())
n = int(n)
m = int(m)

# Initialize the room grid
room = []
for i in range(n):
    room.append(list(input().strip()))

# Initialize the set to store the characters found
ans = set()

# Iterate through the room grid to find the characters adjacent to `col`
for i in range(n):
    for j in range(m):
        if room[i][j] == col:
            for k in range(4):
                tox = i + dirx[k]
                toy = j + diry[k]
                if valid(tox, toy) and room[tox][toy] != col and room[tox][toy] != '.':
                    ans.add(room[tox][toy])

# Print the size of the set
print(len(ans))
