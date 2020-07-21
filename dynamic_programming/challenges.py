class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def lcs(strA, strB):
    if len(strB) == 0 or len(strA) == 0:
        return 0
    elif strB[-1] == strA[-1]:
        return 1 + lcs(strA[:-1], strB[:-1])
    else: 
        return max(
            lcs(strA[:-1], strB), lcs(strA, strB[:-1])
        )


def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    num_columns = len(strB) + 1
    num_rows = len(strA) + 1

    dynamic_programming_table = [
        [
            0
            for j in range(num_columns)
        ]
        for i in range(num_rows)
    ]

    for i in range(1, num_rows):
        for j in range(1, num_columns):
            if strA[i-1] == strB[j-1]:
                dynamic_programming_table[i][j] = dynamic_programming_table[i-1][j-1] + 1
            else:
                dynamic_programming_table[i][j] = max(
                    dynamic_programming_table[i-1][j],
                    dynamic_programming_table[i][j-1]
                )

    return dynamic_programming_table[num_rows-1][num_columns-1]




def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if rows == 0 or cols == 0:
                dp_table[row][col] = 0

            elif items[row-1][1] > col:
                dp_table[row][col] = dp_table[row-1][col]

            else:
                value_with = items[row-1][2] + dp_table[row-1][col - items[row-1][1]]
                value_without = dp_table[row-1][col]
                dp_table[row][col] = max(value_with, value_without)

    return dp_table[rows-1][cols-1]


def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.
    for row in range(rows):
        for col in range(cols):
            if rows == 0 or cols == 0:
                dp_table[row][col] = 0

            elif items[row-1][1] > col:
                dp_table[row][col] = dp_table[row-1][col]

            else:
                value_with = items[row-1][2] + dp_table[row-1][col - items[row-1][1]]
                value_without = dp_table[row-1][col]
                dp_table[row][col] = max(value_with, value_without)

    return dp_table[rows-1][cols-1]


@Memoize
def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    if len(str1) == 0 or len(str2) == 0:
        return max(len(str1), len(str2))

    modify = edit_distance(str1[:-1], str2[:-1])

    if str1[-1] == str2[-1]:
        return modify

    insert = edit_distance(str1, str2[:-1])
    delete = edit_distance(str1[:-1], str2)

    return 1 + min(insert, delete, modify)


def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if row == 0 or col == 0:
                dp_table[row][col] = max(row, col)
            else:
                if str1[row - 1] == str2[col - 1]:
                    dp_table[row][col] = dp_table[row - 1][col - 1]
                else:
                    replace = dp_table[row - 1][col - 1]
                    insert = dp_table[row][col - 1]
                    delete = dp_table[row - 1][col]
                    dp_table[row][col] = min(replace, insert, delete) + 1
    
    return dp_table[rows-1][cols-1]
