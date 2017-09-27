from lib.coordinate import Coordinate
from lib.direction import Direction
from collections import deque
from itertools import groupby
from functools import reduce
from lib.piece import Piece
from lib.board import Board
from lib.color import Color
from copy import copy
# For cleaner reduction and code reusability
from operator import add, sub

# Counts distinct sets on the board
# Of a specific color
# Where num pieces are adjacent to one another
# (No more no less)
def sets_of_adjacent(color_set):
    visited = [{}, {}, {}, {}]
    scores = {1:0, 2:0, 3:0, 4:0, 5:0}
    keys = list(color_set.keys())
    keys.sort()
    for coord in keys:
        if coord not in visited[Direction.LD.value]:
            count = traverse_successors(coord, Direction.LD, color_set, visited)
            scores[count] += 1
        if coord not in visited[Direction.V.value]:
            count = traverse_successors(coord, Direction.V, color_set, visited)
            scores[count] += 1
        if coord not in visited[Direction.RD.value]:
            count = traverse_successors(coord, Direction.RD, color_set, visited)
            scores[count] += 1
        if coord not in visited[Direction.H.value]:
            count = traverse_successors(coord, Direction.H, color_set, visited)
            scores[count] += 1

    return scores


def traverse_successors(coord, direction, color_set, visited, count=1):
    successor = get_successor(coord, direction)
    if count == 5 or successor not in color_set: return count 

    visited[direction.value][successor] = True
    return traverse_successors(successor, direction, color_set, visited, count + 1)

def get_successor(coord, direction):
    if direction == Direction.H:
        return Coordinate.copy_with_new_x(coord, coord.x + 1)
    elif direction == Direction.V:
        return Coordinate.copy_with_new_y(coord, coord.y + 1)
    elif direction == Direction.LD:
        return Coordinate(coord.x - 1, coord.y + 1)
    elif direction == Direction.RD:
        return Coordinate(coord.x + 1, coord.y + 1)
