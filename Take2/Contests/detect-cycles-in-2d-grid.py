#https://leetcode.com/contest/biweekly-contest-33/problems/detect-cycles-in-2d-grid
class Solution:
    def cycle_detector(self, prev_node, curr_node, is_cycle, visited, grid):
        if prev_node:
            visited.add(prev_node)
        
        neighbours = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        has_children = False
        for neighbour in neighbours:
            nx = curr_node[0] + neighbour[0]
            ny = curr_node[1] + neighbour[1]
            loc = (nx, ny)
            if ( 0 <= nx < len(grid) and
                 0 <= ny < len(grid[nx]) and
                 grid[nx][ny] == grid[curr_node[0]][curr_node[1]] and
                 loc != prev_node):
                if loc in visited:
                    return True
                has_children = True
                is_cycle = self.cycle_detector(curr_node, loc, is_cycle, visited, grid)
                if is_cycle:
                    return True
        if not has_children:
            visited.add(curr_node)
        return False
        
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (row, col) not in visited:
                    is_cycle = self.cycle_detector(None, (row, col), False, visited, grid)
                    if is_cycle:
                        return True
        return False
