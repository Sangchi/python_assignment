class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gidct=gdict

    def addEdge(self,vertex,edge):
        self.gidct[vertex].append(edge)

    def dfs(self,vertex):
        visited=[vertex]
        stack=[vertex]
        while stack:
            popVertex=stack.pop()
            print(popVertex)
            for adjacentvertex in self.gidct[popVertex]:
               if adjacentvertex not in visited:
                visited.append[adjacentvertex]
                stack.append[adjacentvertex]


coustmerdict={"a":["b","c"],
              "b":["a","d","e"],
              "c":["a","e"],
              "d":["b","e","f"],
              "e":["d","f"],
              "f":["d","e"]} 
                
Graph=graph(coustmerdict)
Graph.dfs("a")



        