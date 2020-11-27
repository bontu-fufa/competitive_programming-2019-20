#https://leetcode.com/contest/biweekly-contest-33/problems/minimum-number-of-vertices-to-reach-all-nodes
class Solution:  
  def dfs(self, curr_node, is_parented, dp, visited, graph):
      if curr_node in visited:
          dp[curr_node]["is_parented"] = True
          return dp[curr_node]
      visited.add(curr_node)
      all_reachable = {curr_node}
      for child in graph[curr_node]:
          all_reachable.union(self.dfs(child, True, dp, visited, graph)["all_reachable"])

      dp[curr_node] = {"all_reachable": all_reachable, "is_parented": is_parented}
      return dp[curr_node]
  def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
      graph = [[] for i in range(n)]
      for edge in edges:
          graph[edge[0]].append(edge[1])

      visited = set()
      # {all_reachable: {}, is_parented: Bool}
      dp = {}
      for node in range(n):
          if node not in visited:
              self.dfs(node, False, dp, visited, graph)

      result_vertices  = []
      for node in range(n):
          if not dp[node]["is_parented"]:
              result_vertices.append(node)

      return result_vertices 
