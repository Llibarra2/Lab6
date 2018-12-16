'''
Lester Ibarra
80578839
Diego Aguirre

The following shows Kruskal's algorithm finding the best path of the hard coded graph
'''
  
class Graph: 
  
    def __init__(self,vertices): 
        self.vertex= vertices #No. of vertices 
        self.graph = [] # default graph storage
          
   
    def addEdge(self,u,v,w):    # function to add an edge to graph 
        self.graph.append([u,v,w]) 
  
    
    def find(self, parent, i): # A utility function to find set of an element i 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    def union(self, parent, rank, x, y): #The method creates a uinon between the given vertices
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        if rank[xroot] < rank[yroot]:         # Attach smaller rank tree under root of   high rank tree (Union by Rank) 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        else :        # If ranks are same, then make one as root and increment its rank by one 
            parent[yroot] = xroot 
            rank[xroot] += 1
  
    def Kruskals(self):  # The main function to construct MST using Kruskal's  
  
        result =[] #This will store the resultant MST 
  
        edge = 0 # An index variable, used for sorted edges 
        index = 0 # An index variable, used for result[] 
  
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] 
        rank = [] 
  
        # Create V subsets with single elements 
        for node in range(self.vertex): 
            parent.append(node) 
            rank.append(0) 
      
        # Number of edges to be taken is equal to V-1 
        while index < self.vertex -1 :#selects the smallest edge
            u,v,w =  self.graph[edge] 
            edge = edge + 1
            start = self.find(parent, u) 
            end = self.find(parent ,v) 
  
            if start != end: #appends edge if no cycle is created
                index = index + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, start, end)             
            # Else discard the edge 
  
        print ("Best path (Kruskals): ")
        for src,dest,weight  in result: 
            print ("%d -- %d == %d" % (src,dest,weight)) 
  
def main():# Driver code 
    test = Graph(5) 
    test.addEdge(0, 1, 7)#the method in which information is used to create an edege using a source, destination, weight
    test.addEdge(0, 2, 3) 
    test.addEdge(0, 3, 5) 
    test.addEdge(1, 3, 13) 
    test.addEdge(2, 3, 4)
    test.addEdge(4, 2, 2)
    test.Kruskals()#executes kruskals method into graph
main()
