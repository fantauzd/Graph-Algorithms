# Apply Graph traversal to solve a problem (Portfolio Project Problem):
# You are given a 2-D puzzle of size MxN, that has N rows and M column (M and N can be
# different). Each cell in the puzzle is either empty or has a barrier. An empty cell is marked by
# ‘-’ (hyphen) and the one with a barrier is marked by ‘#’.
#
# You are given two coordinates from the puzzle (a,b) and (x,y).
# You are currently located at (a,b) and want to reach (x,y).

# You can move only in the following directions.
# L: move to left cell from the current cell
# R: move to right cell from the current cell
# U: move to upper cell from the current cell
# D: move to the lower cell from the current cell

# You can move to only an empty cell and cannot move to a cell with a barrier in it. Your goal
# is to reach the destination cells covering the minimum number of cells as you travel from the
# starting cell.

# Input: puzzle, source, destination.
# Puzzle: A list of lists, each list represents a row in the rectangular puzzle. Each
# element is either ‘-’ for empty (passable) or ‘#’ for obstacle (impassable). The same
# as in the example.
# Puzzle = [
#  ['-', '-', '-', '-', '-'],
#  ['-', '-', '#', '-', '-'],
#  ['-', '-', '-', '-', '-'],
#  ['#', '-', '#', '#', '-'],
#  ['-', '#', '-', '-', '-']
# ]

# source: A tuple representing the indices of the starting position, e.g. for the upper right corner, source=(0, 4).

# destination: A tuple representing the indices of the goal position, e.g. for the lower right corner, goal=(4, 4).

# Output: A list of tuples representing the indices of each position in the path. The first tuple
# should be the starting position, or source, and the last tuple should be the destination. If
# there is no valid path, None should be returned. Not an empty list, but the None object. If
# source and destination are same return the same cell.


# we will use a deque to access first and last cells
from collections import deque


def solve_puzzle(board, source, destination):
    """
    Solves the puzzle problem outlined above.
    :param board: A list of lists, each list represents a row in the rectangular puzzle. Each
    element is either ‘-’ for empty (passable) or ‘#’ for obstacle (impassable).
    :param source: A tuple representing the indices of the starting position
    :param destination: A tuple representing the indices of the goal position
    :return:
    """
    # store the bounds of the puzzle
    rows, columns = len(board), len(board[0])

    queue = deque([])
    # add the starting point to our queue
    queue.append(source)

    # track visited cells, we will consider a cell visited after it has been processed, start at source
    visited = [[False] * columns for i in range(rows)]
    visited[source[0]][source[1]] = True

    # track previous cells in dictionary for easy overwrites
    previous_cell = {}

    # try left, up, right, down
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    # process each cell in the queue until we arrive at the destination
    while queue:
        cur = queue.popleft()
        row, col = cur[0], cur[1]

        # if we reached the end, don't process cell
        if cur == destination:
            break

        for x_move, y_move in directions:
            new_row, new_col = row + x_move, col + y_move
            # skip any invalid directions
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= columns:
                continue
            # skip any blocked cells
            if board[new_row][new_col] == '#':
                continue
            # skip cells that have already been visited
            if not visited[new_row][new_col]:
                visited[new_row][new_col] = True
                # enqueue each new neighboring cell
                queue.append((new_row, new_col))
                # remember that we arrived at the cell from current cell
                previous_cell[(new_row, new_col)] = cur

    # previous_cell now holds all the reachable cells as keys and the prev cell as value
    if destination not in previous_cell:  # O(N) check as prev cell might hold all cells from board, N = rows * columns
        return None, None

    # now we must use the previous_cell dictionary to decode the path taken to destination
    path = [destination]
    path_string = ''
    directions_dict = {(0, -1): 'L', (-1, 0): 'U', (0, 1): 'R', (1, 0): 'D'}
    # backtrack until we reach the starting point
    while path[-1] != source:
        # find the direction taken from back step to current and add it to string
        previous_row, previous_col = previous_cell[path[-1]]
        diff_row = path[-1][0] - previous_row
        diff_col = path[-1][1] - previous_col
        path_string += directions_dict[(diff_row, diff_col)]
        # find the cell before the current cell
        back_step = previous_cell[path[-1]]
        # add it to out path
        path.append(back_step)

    # make sure the path and string start at the first cell
    res = path[::-1]
    res_string = path_string[::-1]
    return (res, res_string)

if __name__ == '__main__':
    b1 = [
        ['-','-','-','-','-'],
        ['-','-','#','-','-'],
        ['-','-','-','-','-'],
        ['#','-','#','#','-'],
        ['-','#','-','-','-']
    ]
    s1 = (0,2)
    d1 = (2,2)
    print(solve_puzzle(b1, s1, d1))
    s2 = (0,0)
    d2 = (4,4)
    print(solve_puzzle(b1, s2, d2))
    b2 = [
        ['-', '#', '-'],
        ['-', '-', '-'],
        ['#', '#', '-']
    ]
    print(solve_puzzle(b2, s1, d1))
    print(solve_puzzle(b2, s2, d1))
    b3 = [
        ['-', '#', '-'],
        ['-', '-', '#'],
        ['#', '#', '-']
    ]
    print(solve_puzzle(b3, s2, d1))
