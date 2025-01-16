from collections import deque

def shortestPath(grid, k):
        q = deque()
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        q.append((0, 0, k, 0))
        visited.add((0, 0, k))

        while q:
            i, j, removal_remaining, steps = q.popleft()

            if (i, j) == (m-1, n-1):
                return steps
            for dx, dy in directions:
                new_id_x = i + dx
                new_id_y = j + dy
                if 0 <= new_id_x < m and 0 <= new_id_y < n:
                    # as grid[new_id_x][new_id_y] will 0 or 1 
                    new_removal_remaining = removal_remaining - grid[new_id_x][new_id_y]
                    new_set = (new_id_x, new_id_y, new_removal_remaining)

                    if new_removal_remaining >= 0 and new_set not in visited:
                        q.append((new_id_x, new_id_y, new_removal_remaining, steps + 1))
                        visited.add(new_set)

        return -1