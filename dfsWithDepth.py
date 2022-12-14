from typing import List

from webcolors import rgb_to_hex

from abstractClass import ABCClass


class DFSWithDepth(ABCClass):
    used: List
    max_depth: int = 0

    def find_shortest_path(self, start, end):
        self.used = [0 for _ in range(self.n)]
        start_idx, end_idx = self.set_default(start, end)
        self.depth_assessment(start_idx)
        self.dfs_with_depth(start_idx, self.max_depth)
        path = self.build_path(end_idx)
        self.draw_graph(self.get_method())
        self.save_graph(self.get_method())
        print('{}: {}'.format(self.get_method(), self.iteration_counter))
        return list(map(lambda x: self.idx_to_city[x], path))

    def depth_assessment(self, node, depth=1):
        self.used[node] = 1
        self.max_depth = max(self.max_depth, depth)
        for city_idx, distance in self.adj_matrix[node]:
            if self.used[city_idx] == 0:
                self.depth_assessment(city_idx, depth + 1)

    def dfs_with_depth(self, node, depth):
        self.increment_iter_cnt()
        if depth <= 0:
            return
        for city_idx, distance in self.adj_matrix[node]:
            if self.dist[city_idx] > self.dist[node] + distance:
                self.dist[city_idx] = self.dist[node] + distance
                self.parent[city_idx] = node
                self.G.add_edge(
                    self.idx_to_city[node],
                    self.idx_to_city[city_idx],
                    weight=distance,
                    color=rgb_to_hex((self.red_value, self.green_value, self.blue_value))
                )
                self.increment_color(1)
                self.dfs_with_depth(city_idx, depth - 1)

    def get_method(self):
        return 'DFS with depth'
