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


if __name__ == "__main__":

    graph = {"a":["b","c","d"],
            "b":["a","d","e"],
            "c":["a","f"],
            "d":["a","b","f"],
            "e":["b","f","h"],
            "f":["c","d","e","g"],
            "g":["f","h","i"],
            "h":["e","g","i"],
            "i":["g","h"]
            }
    start = "a"
    goal = "i"

    search = GraphSearch(graph,start,goal)

    print("BFS:  ", search.bfs())
    print("DFS:  ", search.dfs())

