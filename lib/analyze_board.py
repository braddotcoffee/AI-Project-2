from lib.coordinate import Coordinate
from itertools import groupby
from functools import reduce
from lib.piece import Piece
from lib.board import Board
from lib.color import Color
# For cleaner reduction and code reusability
from operator import add, sub
from copy import copy

# Counts distinct sets on the board
# Of a specific color
# Where num pieces are adjacent to one another
# (No more no less)
def sets_of_adjacent(num, color_set):
    return sets_by_row(num, color_set) + sets_by_col(num, color_set) \
            + sets_by_diag(num, color_set)

# Group like elements by their y value (same row)
# Count by their x value (iterating rows)
def sets_by_row(num, color_set):
    coords = list(color_set.keys())
    coords.sort(key=lambda coord : coord.y)
    return sets_by_orth(num, coords, "y", "x")

# Group like elements by their x value (same row)
# Count by their y value (iterating rows)
def sets_by_col(num, color_set):
    coords = list(color_set.keys())
    coords.sort(key=lambda coord : coord.x)
    return sets_by_orth(num, coords, "x", "y")

def sets_by_orth(num, coords, group_attr, count_attr):
    # Group into 2D array of Coordinates w/ equivalent row
    grouped_coords = [ list(equal) for num, equal in groupby(coords, lambda coord : getattr(coord, group_attr)) ]
    counts = [check_orthogonal(num, orth, count_attr) for orth in grouped_coords]
    return reduce(add, counts, 0)

# Counts number of sets of exactly length num
# Are in orth
def check_orthogonal(num, orth, attr):
    orth.sort(key=lambda coord : getattr(coord, attr))
    count = 0 # Number found of correct length
    curr_found = 1 # Current found in a row
    for i in range(len(orth)-1):
        if getattr(orth[i], attr) + 1 == getattr(orth[i + 1], attr):
            curr_found += 1
            if curr_found == 5: return 1
        elif curr_found == num:
            count += 1
            curr_found = 1 # Reset
        else:
            curr_found = 1 # Reset
    if curr_found == num: count += 1
    return count

def sets_by_diag(num, color_set):
    return check_diagonal(num, color_set, add, add) + check_diagonal(num, color_set, sub, add)

def check_diagonal(num, color_set, op_row, op_col):
    color_set = copy(color_set)
    keys = list(color_set.keys())
    if len(keys) == 0: return 0
    keys.sort()
    count = 0
    curr_found = 1
    visited = {}
    temp_row, temp_col = get_start_coord(keys, visited)
    while len(keys) > 0 and within_bounds(temp_row) and within_bounds(temp_col):
        temp_row = op_row(temp_row, 1)
        temp_col = op_col(temp_col, 1)
        coord = Coordinate(temp_row, temp_col)
        visited[coord] = True
        if coord in color_set:
            curr_found += 1
            if curr_found == 5: return 1
        elif curr_found == num:
            count += 1
            curr_found = 1
            temp_row, temp_col = get_start_coord(keys, visited)
        else:
            temp_row, temp_col = get_start_coord(keys, visited)
            curr_found = 1
    if curr_found == num: count += 1
    return count


def within_bounds(val):
    return val > 0 and val < 14

def get_start_coord(keys, visited):
    for key in keys:
        if key not in visited: return key.x, key.y
    return False, False

