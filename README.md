# Graph-Search
BFS,DFS,Djikstra and A*

# Input :

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
            
# BFS :

['a', 'b', 'c', 'd', 'e', 'f', 'h', 'g', 'i']
# DFS:   

['a', 'b', 'e', 'f', 'g', 'i']
