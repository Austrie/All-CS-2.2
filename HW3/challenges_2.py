from collections import deque

def is_valid_keys(grid, i, j) -> bool:
    return (i >= 0) and (i < len(grid)) and (j >= 0) and (j < len(grid[0]))

def timeToRot(grid):
    """
    Take in a grid of numbers, where 0 is an empty space, 1 is a fresh orange, and 2 is a rotten
    orange. Each minute, a rotten orange contaminates its 4-directional neighbors. Return the number
    of minutes until all oranges rot.
    """
    queue = deque()
    fresh_oranges = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                queue.append((i,j))
            elif grid[i][j] == 1:
                fresh_oranges += 1
            
                
    minutes_needed = 0
    while queue:
        newly_rotten_oranges = []
        while queue:
            (i,j) = queue.pop()
            for neighbor_i_j in [(i+1, j),(i-1, j),(i, j+1),(i, j-1)]:
                neighbor_i, neighbor_j = neighbor_i_j
                if is_valid_keys(grid, neighbor_i, neighbor_j) and (
                    grid[neighbor_i][neighbor_j] == 1
                ):
                    newly_rotten_oranges.append((neighbor_i, neighbor_j))
                    grid[neighbor_i][neighbor_j] = 2
                    fresh_oranges -= 1
                    
                    
        if newly_rotten_oranges:
            queue.extend(newly_rotten_oranges)
            minutes_needed += 1
        
    return minutes_needed if fresh_oranges == 0 else -1

  

# Test Cases
oranges1 = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
answer = timeToRot(oranges1)
print("oranges1 answer:", answer)
assert answer == 4

oranges2 = [
    [2,1,1],
    [0,1,1],
    [1,0,1]
]
answer = timeToRot(oranges2)
print("oranges2 answer:", answer)
assert answer == -1

oranges3 = [
    [0,2]
]
answer = timeToRot(oranges3)
print("oranges3 answer:", answer)
assert answer == 0

