# Python3 program to print Vertex Cover
# of a given undirected graph 
from collections import defaultdict 

# This class represents a directed graph 
# using adjacency list representation 
class Graph:

	def __init__(self, vertices):
		
		# No. of vertices
		self.V = vertices 
		
		# Default dictionary to store graph
		self.graph = defaultdict(list) 

	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# The function to print vertex cover 
	def printVertexCover(self):
		
		# Initialize all vertices as not visited. 
		visited = [False] * (self.V)
		
		# Consider all edges one by one 
		for u in range(self.V):
			
			# An edge is only picked when 
			# both visited[u] and visited[v] 
			# are false
			if not visited[u]:
				
				# Go through all adjacents of u and 
				# pick the first not yet visited 
				# vertex (We are basically picking
				# an edge (u, v) from remaining edges. 
				for v in self.graph[u]:
					if not visited[v]:
						
						# Add the vertices (u, v) to the
						# result set. We make the vertex
						# u and v visited so that all 
						# edges from/to them would 
						# be ignored 
						visited[v] = True
						visited[u] = True
						break

		# Print the vertex cover 
		for j in range(self.V):
			if visited[j]:
				print(j, end = ' ')
				
		print()

# Driver code

# Create a graph given in 
# the above diagram 
g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(3, 4) 
g.addEdge(4, 5) 
g.addEdge(5, 6) 

g.printVertexCover()


