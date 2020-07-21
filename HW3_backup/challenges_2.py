# Problem 2
def timeToRot(grid):
    """
    Take in a grid of numbers, where 0 is an empty space, 1 is a fresh orange, and 2 is a rotten
    orange. Each minute, a rotten orange contaminates its 4-directional neighbors. Return the number
    of minutes until all oranges rot.
    """
    if grid is None or len(grid) == 0 or len(grid[0]) == 0:
      return 0

    time_taken_to_rot_dict = {
      i: {
        j: grid[i][j] + -2 #0 if grid[i][j] == 2 else (-1 if == 1 else -2)
        for j in range(0, len(grid[i]))
      }
      for i in range(0, len(grid))
    }
    for i in range(0, len(grid)):
      for j in range(0, len(grid[i])):
        if grid[i][j] == 1:
          time_to_rot_helper(grid, time_taken_to_rot_dict, i, j)

    times = set([
      time_taken_to_rot_dict[i][j]
      for j in time_taken_to_rot_dict[i]
      for i in time_taken_to_rot_dict
    ])
    max_time = max(list(times))
    return -1 if -1 in times else max_time



def is_valid_keys(grid, i, j) -> bool:
  return (i >= 0) and (i < len(grid)) and (j >= 0) and (j < len(grid[0]))


def time_to_rot_helper(grid, time_taken_to_rot_dict, i, j):
  valid_keys = is_valid_keys(grid, i, j)
  if not valid_keys or time_taken_to_rot_dict[i][j] > -1 or grid[i][j] == 0:
    return -1

  next_to_slot = max(
    [
      time_taken_to_rot_dict[i + 1][j],
      time_taken_to_rot_dict[i - 1][j],
      time_taken_to_rot_dict[i][j + 1],
      time_taken_to_rot_dict[i][j - 1],
    ]
  )
  if next_to_slot > -1:
    time_taken_to_rot_dict[i][j] = next_to_slot + 1

  return time_taken_to_rot_dict[i][j]


  

# Test Cases
oranges1 = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
assert timeToRot(oranges1) == 4

oranges2 = [
    [2,1,1],
    [0,1,1],
    [1,0,1]
]
assert timeToRot(oranges2) == -1

oranges3 = [
    [0,2]
]
assert timeToRot(oranges3) == 0

