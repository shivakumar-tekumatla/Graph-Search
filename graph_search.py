from sys import maxsize as inf 
class GraphSearch:
    def __init__(self,graph,start,goal) -> None:
        self.graph = graph 
        self.start = start 
        self.goal = goal 
        pass

    def bfs(self):
        # self.__init__()
        queue = [] 
        visited = set() #stores all the visited nodes 

        queue.append(self.start) 
        path = [] 

        while queue:
            node = queue.pop(0)
            path.append(node)
            if node == self.goal:
                return path
            visited.add(node)
            for vertex in self.graph[node]:
                if vertex not in visited:
                    if vertex not in queue:
                        queue.append(vertex)
                
        return None #No path found 
         
    def dfs(self):
        queue = []
        visited = set()
        path =[]
        queue.append(self.start)
        while queue:
            node = queue.pop(0)
            path.append(node)
            if node== self.goal:
                return path
            visited.add(node)
            idx = 0 
            for vertex in self.graph[node]:
                if vertex not in visited:
                    if vertex not in queue:
                        queue.insert(idx,vertex) #inserting at the start idx 
                        idx+=1 

        return None 

    def djikstra(self):
        node_cost = {node: inf for node in self.graph}
        node_cost[self.start] = 0
        queue = set(self.graph)
        previous = {node: None for node in self.graph} #keep track to generate path 

        while queue:
            node = min(queue, key=lambda node: node_cost[node])
            queue.remove(node)

            if node == self.goal:
                break

            for vertex in self.graph[node]:
                edge_cost = self.graph[node][vertex]
                if edge_cost + node_cost[node] < node_cost[vertex]:
                    node_cost[vertex] = edge_cost + node_cost[node]
                    previous[vertex] = node

        path = []
        node = self.goal
        while node:
            path.append(node)
            node = previous[node]
        if path[-1] != start: #if no path 
            return None , inf

        return path[::-1], node_cost[self.goal], 





       


if __name__ == "__main__":

    undirected_graph = {"a":["b","c","d"],
            "b":["a","d","e"],
            "c":["a","f"],
            "d":["a","b","f"],
            "e":["b","f","h"],
            "f":["c","d","e","g"],
            "g":["f","h","i"],
            "h":["e","g","i"],
            "i":["g","h"]
            }
    directed_graph = {"a":{"b":2,"d":3,"c":2},
                      "b":{"e":5},
                      "c":{"a":2,"f":1},
                      "d":{"b":1,"f":2},
                      "e":{"h":6},
                      "f":{"e":1,"g":7},
                      "g":{"h":1},
                      "h":{"i":3},
                      "i":{"g":5}
                    }

    start = "a"
    goal = "i"

    search = GraphSearch(directed_graph,start,goal)

    print("BFS:  ", search.bfs())
    print("DFS:  ", search.dfs())
    print("Djikstra:  ", search.djikstra())

    

