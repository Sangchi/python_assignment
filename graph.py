from ast import Break
from asyncio.windows_events import NULL


class graph:
    def __init__(self,gdict=None):
         if gdict is None:
          gdict={}
         self.gdict=gdict

    def addEdge(self,vertex,edge):
         self.gdict[vertex].append(edge)
  
    def bfs(self,vertex):
          visited=[vertex]
          queue=[vertex]
          while queue:
               devertex=queue.pop(0)
               print(devertex)
               for adjacentvertex in self.gdict[devertex]:
                   if adjacentvertex not in visited:
                      visited.append(adjacentvertex)  
                      queue.append(adjacentvertex)

          

     
costmerdict={"a":["b","c"],
                 "b":["a","d","e"],
                 "c":["a","e"],
                 "d":["b","e","f"],
                 "e":["d","f"],
                 "f":["d","e"]   }

Graph =graph(costmerdict)
Graph.bfs("a")



        
