from collections import deque
import heapq

class unionfind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.num = [1] * n

    def find_root(self, change_list, vertex):
        value = self.parent[vertex]
        if value < 0:
            return vertex
        else:
            change_list.append(vertex)
            return self.find_root(change_list, value)

    def set_find(self, vertex):
        change_list = list()
        root = self.find_root(change_list, vertex)

        for i in change_list:
            self.parent[i] = root

        return root

    def set_union(self, u_set, v_set):
        if self.num[u_set] < self.num[v_set]:
            self.parent[u_set] = v_set
            self.num[v_set] += self.num[u_set]
        else:
            self.parent[v_set] = u_set
            self.num[u_set] += self.num[v_set]

def solution(land, height):
    n = len(land)
    move_list = [[-1, 0],[1, 0],[0, -1],[0, 1]]
    game_map = [[0] * (n + 2) for _ in range(n + 2)]
    index_map = [[None] * (n + 2) for _ in range(n + 2)]
    index = -1

    for i in range(n): 
        for j in range(n): 
            index_map[i+1][j+1] = -1
            game_map[i+1][j+1] = land[i][j]

    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if index_map[y][x] == -1:
                index = index + 1
                index_map[y][x] = index
                dfs = deque([[y, x]])

                while dfs:
                    temp_y, temp_x = dfs.popleft()
                    for move in move_list:
                        next_y, next_x = temp_y + move[0], temp_x + move[1]
                        if index_map[next_y][next_x] == -1:
                            if abs(game_map[temp_y][temp_x] - game_map[next_y][next_x]) <= height:
                                dfs.append([next_y, next_x])
                                index_map[next_y][next_x] = index

    priority_queue = []
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            for move in [[0, 1],[1, 0]]:
                next_y, next_x = y + move[0], x + move[1]
                if index_map[y][x] != index_map[next_y][next_x] != None:
                    heapq.heappush(priority_queue, [abs(game_map[y][x] - game_map[next_y][next_x]),index_map[y][x], index_map[next_y][next_x]])
                    pass

    answer = 0
    union_find = unionfind(n * n)

    while priority_queue:
        weight, u, v = heapq.heappop(priority_queue)
        u_set, v_set = union_find.set_find(u), union_find.set_find(v)
        if u_set != v_set:
            answer += weight
            union_find.set_union(u_set, v_set)

    return answer
