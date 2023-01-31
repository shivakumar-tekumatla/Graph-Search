# Graph-Search
BFS,DFS,Djikstra and A*

# Input :

            undirected_graph = 
           
                       {

                        "a":["b","c","d"],

                        "b":["a","d","e"],

                        "c":["a","f"],

                        "d":["a","b","f"],

                        "e":["b","f","h"],

                        "f":["c","d","e","g"],

                        "g":["f","h","i"],

                        "h":["e","g","i"],

                        "i":["g","h"]

                        }
            directed_graph =
                        {
                            "a":{"b":2,"d":3,"c":2},

                            "b":{"e":5},

                            "c":{"a":2,"f":1},

                            "d":{"b":1,"f":2},

                            "e":{"h":6},

                            "f":{"e":1,"g":7},

                            "g":{"h":1},

                            "h":{"i":3},

                            "i":{"g":5}
                        }

For these results , directed graph is the input.  
# BFS :

            ['a', 'b', 'd', 'c', 'e', 'f', 'h', 'g', 'i']

# DFS:   

            ['a', 'b', 'e', 'h', 'i']

# Djikstra 

            (['a', 'c', 'f', 'e', 'h', 'i'], 13)
