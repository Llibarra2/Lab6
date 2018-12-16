'''
Lester Ibarra
80578839
Diego Aguirre

This program will implement topological sort into a hardcoded given graph in order to
determine the best path for the graph, meaning the least amount of weight
'''
#Python program to print topological sorting of a DAG 
from collections import defaultdict 
  
class Graph: #class made for a graph data structure
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.vertex = vertices #number of vertices
  
    # A recursive function used by topologicalSort 
    def topologicalSortUtil(self,src,visited,stack): 
        visited[src] = True
  
        for i in self.graph[src]:#goes through all vertices of the given graph
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
        stack.insert(0,src)#pushes vertex into stack
  
    # function to add an edge to graph 
    def Add_Edge(self,u,v): 
        self.graph[u].append(v) 
  
    
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.vertex
        stack =[] 
  
        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for i in range(self.vertex): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Print contents of the stack 
        print (stack)
def main():
    test= Graph(6) 
    test.Add_Edge(5, 2); 
    test.Add_Edge(5, 0); 
    test.Add_Edge(4, 0); 
    test.Add_Edge(4, 1); 
    test.Add_Edge(2, 3); 
    test.Add_Edge(3, 1); 
      
    print ("Path of given graph: ")
    test.topologicalSort()
main()
