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
          
    
    def find(self, parent, i): # A utility function to find set of an element i 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    def union(self, parent, rank, x, y): #The method creates a uinon between the given vertices
        root1 = self.find(parent, x) 
        root2 = self.find(parent, y) 
  
        if rank[root1] < rank[root2]:         # Attach smaller rank tree under root of   high rank tree (Union by Rank) 
            parent[root1] = root2 
        elif rank[root1] > rank[root2]: 
            parent[root2] = root1 
  
        else :        # If ranks are same, then make one as root and increment its rank by one 
            parent[root2] = root1 
            rank[root1] += 1
    
    def Add_Edge(self,src,dest,weight):    # function to add an edge to graph 
        self.graph.append([src,dest,weight]) 
  
  
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
            src,dest,weight =  self.graph[edge] 
            edge = edge + 1
            start = self.find(parent, src) 
            end = self.find(parent,dest) 
  
            if start != end: #appends edge if no cycle is created
                index = index + 1     
                result.append([src,dest,weight]) 
                self.union(parent, rank, start, end)             
            # Else discard the edge 
  
        print ("Best path (Kruskals): ")#the following prints Kruskals path
        for src,dest,weight  in result: 
            print ("%d -- %d == %d" % (src,dest,weight)) 
  
def main():# Driver code 
    user = input("\nChoose one of the following options: \nA)Hard Coded\nB)Custom \n")
    if user == 'A' or user == 'a':
        test = Graph(5) 
        test.Add_Edge(0, 1, 7)#the method in which information is used to create an edege using a source, destination, weight
        test.Add_Edge(0, 2, 3) 
        test.Add_Edge(0, 3, 5) 
        test.Add_Edge(1, 3, 13) 
        test.Add_Edge(2, 3, 4)
        test.Add_Edge(4, 2, 2)
        test.Kruskals()#executes kruskals method into graph
    elif user== 'B' or user=='b':
        size = input("Input graph size")
        test = Graph(size)
        for i in range(size):
            src = input("\nChoose source: ")
            dest = input("\nChoose destination: ")
            weight = input("\nChoose weight of edge: ")
            test.Add_Edge(src, dest, weight)
        test.Kruskals()
                
main()
