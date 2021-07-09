# https://leetcode.com/problems/maximal-network-rank/

from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n, roads):
        degree = defaultdict(int)
        adj_matrix = [[0]*n for i in range(n)]
        # Loop to create adjacency matrix and degrees of nodes
        for i in range(len(roads)):
            city_a = roads[i][0]
            city_b = roads[i][1]
            
            # undirected graph
            degree[city_a] += 1
            degree[city_b] += 1
            
            # adjacency matrix formation
            adj_matrix[city_a][city_b] = 1
            adj_matrix[city_b][city_a] = 1
        
        max_rank = 0
        for i in range(n):
            j = i+1
            while j<n:
				# calculating degrees/edges of cities/vertices
                rank = degree[i] + degree[j]
                # Check for two way direction
                if (adj_matrix[i][j]):
                    rank -= 1
                max_rank = max(max_rank, rank)
                j += 1
        return max_rank

s = Solution()
res = s.maximalNetworkRank(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]])
print(res)
