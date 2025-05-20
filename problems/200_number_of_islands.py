'''
# TAG-FLOOD
# N.B.: use DFS/BFS but define the "neighbours" yourself, i.e. with cardinal directions
'''

from typing import List
class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        def isValid(x, y, X, Y):
            if (x >= 0 and x < X) and (y >= 0 and y < Y):
                return True
            else:
                return False

        # classic implementation of dfs w/ custom defn of neighbour (defined by directions)
        def dfs(node, visited, grid):
            stack = [node]
            while stack:
                n = stack.pop()
                
                x,y = n 
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for direction in directions:
                    d_x, d_y = direction
                    new_x = x + d_x
                    new_y = y + d_y
                    neighbour = (new_x, new_y)
                    if (isValid(new_x, new_y, len(grid[0]), len(grid)) is True):
                        if grid[new_y][new_x] == '1' and neighbour not in visited:
                            visited.add(neighbour)
                            stack.append(neighbour)
        
        res = 0
        
        visited = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                v = (x,y)
                if v not in visited and grid[y][x] == '1':
                    dfs(v, visited, grid)
                    res += 1

        return res