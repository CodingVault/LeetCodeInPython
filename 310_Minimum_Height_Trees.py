#!/usr/bin/env python
# encoding: utf-8
"""
310. Minimum Height Trees

Created by Shengwei on 2024-03-11.

Used:
* Meta: https://www.1point3acres.com/bbs/thread-1050777-1-1.html
"""

# https://leetcode.com/problems/minimum-height-trees/description/
# tags: medium / hard, tree, minimum, bfs

"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
 

Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
"""

# https://leetcode.com/problems/minimum-height-trees/solutions/1631179/c-python-3-simple-solution-w-explanation-brute-force-2x-dfs-remove-leaves-w-bfs


# Accepted
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        if n == 1:
            return [0]

        # adjacent matrix
        links = defaultdict(set)
        for e in edges:
            links[e[0]].add(e[1])
            links[e[1]].add(e[0])
        # print('links: {}'.format(links))

        # remove leaves layer by layer
        candidates = [node for node in links if len(links[node]) == 1]
        while candidates:
            leaves = candidates
            candidates = set()
            for leaf in leaves:
                if links[leaf]:  # necessary when there are 2 left
                    adj = links[leaf].pop()
                    links[adj].remove(leaf)
                    if len(links[adj]) == 1:
                        candidates.add(adj)
        
        return list(leaves)



# Opetimized sparse 2-d matrix with defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        if n == 1:
            return [0]

        # adjacent matrix
        links = defaultdict(list)
        for e in edges:
            links[e[0]].append(e[1])
            links[e[1]].append(e[0])
        # print('links: {}'.format(links))

        # breath-first: calculate lengths from each node to others
        buffer, visited = deque([0]), set()
        lengths = defaultdict(dict)
        while buffer:
            current = buffer.popleft()
            visited.add(current)

            for neighbor in links[current]:
                if neighbor not in visited:
                    buffer.append(neighbor)
                    lengths[current][neighbor] = 1
                    lengths[neighbor][current] = 1
                else:
                    for connect, length in lengths[neighbor].items():
                        if connect != current and length:
                            lengths[current][connect] = length + 1
                            lengths[connect][current] = length + 1
        # print('lengths: {}'.format(lengths))

        # max(lengths) is the height of the tree
        counts = defaultdict(set)
        shortest = n
        for node, hs in lengths.items():
            shortest = min(shortest, max(hs.values()))
            counts[max(hs.values())].add(node)
        # print('counts: {}'.format(counts))
        return list(counts[shortest])


# Initial
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []

        # adjacent matrix
        links = defaultdict(list)
        for e in edges:
            links[e[0]].append(e[1])
            links[e[1]].append(e[0])
        # print('links: {}'.format(links))

        # breath-first: calculate lengths from each node to others
        buffer, visited = deque([0]), set()
        lengths = [[0] * n for _ in range(n)]
        while buffer:
            current = buffer.popleft()
            visited.add(current)

            for neighbor in links[current]:
                if neighbor not in visited:
                    buffer.append(neighbor)
                    lengths[current][neighbor] = 1
                    lengths[neighbor][current] = 1
                else:
                    for connect, length in enumerate(lengths[neighbor]):
                        if connect != current and length:
                            lengths[current][connect] = length + 1
                            lengths[connect][current] = length + 1
        # print('lengths: {}'.format(lengths))

        # max(lengths) is the height of the tree
        counts = defaultdict(set)
        shortest = n
        for node, hs in enumerate(lengths):
            shortest = min(shortest, max(hs))
            counts[max(hs)].add(node)
        # print('counts: {}'.format(counts))
        return list(counts[shortest])
