
# Problem 1
def numIslands(grid):
    """Take in a grid of 1s (land) and 0s (water) and return the number of islands."""
    if grid is None or len(grid) == 0 or len(grid[0]) == 0:
      return 0

    seen_dict = {
      i: {
        j: False
        for j in range(0, len(grid[i]))
      }
      for i in range(0, len(grid))
    }
    count = 0
    for i in range(0, len(grid)):
      for j in range(0, len(grid[i])):
        value = grid[i][j]
        if value == 0:
          continue
        else:
          count += num_islands_helper(grid, seen_dict, i, j)
    
    return count

def num_islands_helper(grid, seen_dict, i, j) -> int:
  valid_keys = (i >= 0) and (i < len(grid)) and (j >= 0) and (j < len(grid[0]))
  if not valid_keys or seen_dict[i][j] or grid[i][j] == 0:
    return 0

  seen_dict[i][j] = True
  num_islands_helper(grid, seen_dict, i + 1, j)
  num_islands_helper(grid, seen_dict, i - 1, j)
  num_islands_helper(grid, seen_dict, i, j + 1)
  num_islands_helper(grid, seen_dict, i, j - 1)
  return 1

# Test Cases
map1 = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
result1 = numIslands(map1) 
print('numIslands(map1):', result1)
assert result1 == 1

map2 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
result2 = numIslands(map2) 
print('numIslands(map2):', result2)
assert result2 == 3
