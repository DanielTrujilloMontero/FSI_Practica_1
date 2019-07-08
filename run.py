# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

af = search.GPSProblem('A', 'E'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())

print(search.branch_and_bound(ab).path())
print(search.branch_and_bound_heuristic(ab).path())

print(search.branch_and_bound(af).path())
print(search.branch_and_bound_heuristic(af).path())
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
