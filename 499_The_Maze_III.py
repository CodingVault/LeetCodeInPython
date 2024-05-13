#!/usr/bin/env python
# encoding: utf-8
"""
499. The Maze III

Created by Shengwei on 2025-05-09.

Used:
- TikTok: https://www.1point3acres.com/bbs/thread-1063465-1-1.html
"""

# locked
# tags: hard, matrix, shortest

"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up(u),down(d),left(l) or right(r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving the shortest distance. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the hole (included). Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.

Example 1:

Copy
Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: "lul"

Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.
Both ways have shortest distance 6, but the first way is lexicographically smaller, 
because 'l' < 'u'. So the output is "lul".
Example 2:

Copy
Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (3, 0)

Output: "impossible"

Explanation: The ball cannot reach the hole.
"""

# - https://aaronice.gitbook.io/lintcode/graph_search/the-maze-iii
# - https://xiaoguan.gitbooks.io/leetcode/content/LeetCode/499-The-Maze-III-hard.html


from collections import defaultdict, deque, namedtuple


class Solution:
    def roll(self, matrix, ball_pos, hole_pos):
        """Rolls the all to all possible directions, and records the steps to the stop positions.

        Increases steps to check 1 by 1, with all the paths and positions with such steps.
        """

        def is_valid(pos_x, pos_y):
            return (0 <= pos_x < len(matrix)
                and 0 <= pos_y < len(matrix[0])
                and matrix[pos_x][pos_y] == 0)

        # possible next directions given the current direction;
        # we don't want to roll back and it cannot go further in the same direction
        possible_dirs = {'l': 'ud', 'r': 'ud', 'u': 'lr', 'd': 'lr'}
        dirs = {'l': (0, -1), 'r': (0, 1), 'u': (-1, 0), 'd': (1, 0)}
        queues = defaultdict(deque)
        # key: steps to the positions
        # value: (path, position to reach, next possible directions)
        queues[0].append(('', tuple(ball_pos), 'lrud'))
        visited = {tuple(ball_pos): 0}

        steps = 0
        res = defaultdict(list)

        # increase steps until the count is greater than the max possible steps,
        # also break if the hole could be reached with steps fewer than the next loop
        while steps <= max(queues.keys()) and (not res or min(res.keys()) > steps):
            # check all possible paths to reach stored positions with current steps
            while queues[steps]:
                path, (pos_x, pos_y), next_dirs = queues[steps].popleft()
                for d in next_dirs:
                    move_x, move_y = pos_x, pos_y
                    acc_steps = steps
                    new_path = path + d
                    move = dirs[d]
                    while is_valid(move_x + move[0], move_y + move[1]):
                        acc_steps += 1
                        move_x, move_y = move_x + move[0], move_y + move[1]
                        if (move_x, move_y) == tuple(hole_pos):
                            res[acc_steps].append(new_path)
                            break

                    if (acc_steps <= visited.get((move_x, move_y), acc_steps)
                            and (move_x, move_y) != (pos_x, pos_y)
                            and (move_x, move_y) != tuple(hole_pos)):
                        # if move is possible, and can be reached with fewer or equal steps,
                        # and it's not the hole, record the possible paths
                        # note: need to record new path in case it's lexicographically smaller
                        visited[(move_x, move_y)] = acc_steps
                        queues[acc_steps].append((new_path, (move_x, move_y), possible_dirs[d]))
                    # print(queues)

            steps += 1

        if res:
            # print(res)
            return sorted(res[min(res.keys())])[0]

        return 'impossible'
