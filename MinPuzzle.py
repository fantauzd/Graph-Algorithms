# Dominic Fantauzzo

# You are given a 3-D puzzle. The length and breadth of the puzzle is given by a 2D matrix
# puzzle[m][n]. The height of each cell is given by the value of each cell, the value of
# puzzle[row][column] give the height of the cell [row][column]. You are at [0][0] cell and you
# want to reach to the bottom right cell [m-1][n-1], the destination cell. You can move either
# up, down, left, or right. Write an algorithm to reach the destination cell with minimal effort.
# How effort is defined: The effort of route is the maximum absolute difference between two
# consecutive cells.
# If a route requires us to cross heights: 1, 3, 4, 6, 3, 1
# The absolute differences between consecutive cells is: |1-3| = 2, |3-4|=1, |4-6|=2,
# |6-3|=3, |3-1|=2; this gives us the values: {2, 1, 2, 3, 2}. The maximum value of
# these absolute differences is 3. Hence the effort required on this path will be: 3.
# Example:
# Input: puzzle[][] = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
# Output: 1
# Explanation: The minimal effort route would be [1, 2, 3, 4, 5] which has an effort of
# value 1. This is better than other routes for instance, route [1, 3, 5, 3, 5] which has
# an effort of 2.


# def is_valid(puzzle, x, y):
#     """
#     Checks if a given x,y pair is within a 2d matrix
#     :param puzzle: A 2d matrix
#     :param x: coord
#     :param y: coord
#     :return: Boolean
#     """
#     m, n = len(puzzle), len(puzzle[0])
#     return 0 <= x < m and 0 <= y < n


def minEffort(puzzle):
    """
    Solves the min effort puzzle problem listed above.
    :param puzzle: a 3d puzzle in the form of a 2d array with height values in the cells.
    like puzzle[][] = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
    :return: The minimum possible effort to solve the given puzzle.
    """
    # store the bounds of the puzzle
    m, n = len(puzzle), len(puzzle[0])

    # Initialize a mirror 2d array of puzzle that will store efforts for each cell
    effort_matrix = [([float('inf')] * n ) * m]

    queue = [(0,0)]

    while queue:  # take the next cell
        old_x, old_y = queue.pop(0)
        # try each valid direction
        for x_move, y_move in [(-1, 0), (0, 1), (1, 0), (0, 1)]:
            new_x, new_y = old_x + x_move, old_y + y_move
            if m <= new_x < 0 and n <= new_y < 0:
                continue

            # compare the max effort to get to the cell with the effort for the next step
            old_effort = effort_matrix[old_x][old_y]
            new_effort = abs(puzzle[old_x][old_y] - puzzle[new_x[new_y]])

            # if the new route is not a better solution, move on
            if max(old_effort, new_effort) >= effort_matrix[new_x][new_y]:
                continue

            # Otherwise, update the effort matrix
            effort_matrix[new_x][new_y] = max(old_effort, new_effort)
            queue.append((new_x, new_y))

    #return the effort to get to finish
    return effort_matrix[m - 1][n - 1]

