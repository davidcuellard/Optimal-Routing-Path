#!/usr/bin/env python
# coding: utf-8

# In[32]:


"""
Bournemouth Univeristy
Dept. Computer & Informatics
Search and Optimization
@author: David Cuellar
"""


# In[33]:


#Import libraries
import numpy as np
import pandas as pd
import math


# In[34]:


# In[37]:


class Dijkstras:
    def __init__(self, data, matrix):
        self.data = data
        self.matrix = matrix
        
    def longest(self, source, target0, target1):
        n = len(self.matrix[source])
       
        E2E_T = np.full(n, (-1*np.inf))        
        E2E_T[source] = 0
        
        prev_node = []
                
        node = source
        while (True):
            n_max = 0
            index_max = 0
            if self.matrix[node][target0] != 0 or self.matrix[node][target1] != 0:
                if self.matrix[node][target0] > n_max:
                    n_max = self.matrix[node][target0]
                    index_max = target0
                if self.matrix[node][target1] > n_max:
                    n_max = self.matrix[node][target1]
                    index_max = target1
                
            else:
                for idx, next_node in enumerate(self.matrix[node]):
                    if next_node > n_max and idx not in prev_node:
                        n_max = next_node
                        index_max = idx
            
            prev_node.append(index_max)
            E2E_T[index_max] = n_max
            
            node = index_max
            
            if (node == target0 or node == target1):
                break
            
            if n_max == 0:
                break
        
        def print_route():
            a = []
            for i in range(len(prev_node)):
                a.append([self.data[prev_node][i],E2E_T[prev_node][i]])
            return a
        print(self.data[source], " routing path: ", print_route(), " End-to-end rate: ", min(E2E_T[prev_node])) 


# In[39]: 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[19]:


'''
class Dijkstra:

    def __init__(self, vertices, graph):
        self.vertices = vertices  # ("A", "B", "C" ...)
        self.graph = graph  # {"A": {"B": 1}, "B": {"A": 3, "C": 5} ...}

    def find_route(self, start, end):
        unvisited = {n: float("inf") for n in self.vertices}
        unvisited[start] = 0  # set start vertex to 0
        visited = {}  # list of all visited nodes
        parents = {}  # predecessors
        while unvisited:
            min_vertex = min(unvisited, key=unvisited.get)  # get smallest distance
            for neighbour, _ in self.graph.get(min_vertex, {}).items():
                if neighbour in visited:
                    continue
                new_distance = unvisited[min_vertex] + self.graph[min_vertex].get(neighbour, float("inf"))
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parents[neighbour] = min_vertex
            visited[min_vertex] = unvisited[min_vertex]
            unvisited.pop(min_vertex)
            if min_vertex == end:
                break
        return parents, visited

    @staticmethod
    def generate_path(parents, start, end):
        path = [end]
        while True:
            key = parents[path[0]]
            path.insert(0, key)
            if key == start:
                break
        return path
'''


# In[20]:


'''
input_vertices = ("A", "B", "C", "D", "E", "F", "G")
input_graph = {
    "A": {"B": 5, "D": 3, "E": 12, "F": 5},
    "B": {"A": 5, "D": 1, "G": 2},
    "C": {"E": 1, "F": 16, "G": 2},
    "D": {"A": 3, "B": 1, "E": 1, "G": 1},
    "E": {"A": 12, "C": 1, "D": 1, "F": 2},
    "F": {"A": 5, "C": 16, "E": 2},
    "G": {"B": 2, "C": 2, "D": 1}
}
start_vertex = "B"
end_vertex= "C"
dijkstra = Dijkstra(input_vertices, input_graph)
p, v = dijkstra.find_route(start_vertex, end_vertex)
print("Distance from %s to %s is: %.2f" % (start_vertex, end_vertex, v[end_vertex]))
se = dijkstra.generate_path(p, start_vertex, end_vertex)
print("Path from %s to %s is: %s" % (start_vertex, end_vertex, " -> ".join(se)))
'''


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[21]:


#https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
#https://stackoverflow.com/questions/22897209/dijkstras-algorithm-in-python


# In[22]:


#n = len(self.tr_matrix[self.source])
#E2E_T = np.full(n, (-1*np.inf))
#prev_node = np.full(n, None)

#maxn = 0       
#for x in range(n):
#    if self.tr_matrix[self.source][x] is not None and self.tr_matrix[self.source][x] > max :
#        maxn = self.tr_matrix[x]
#    return maxn


# In[ ]:





# In[23]:


#{‘AA101’, ‘routing path’: (AA113, 43.505), (AA51, 93.854), (LH421, 43.505), (LHR,93.854), End-to-end data rate: ’43.505’}


# In[24]:


# get the start time
#st = time.time()

#Function to test
#distance(df0,df1)

# get the end time
#et = time.time()

# get the execution time
#elapsed_time = et - st
#print('Execution time:', elapsed_time, 'seconds')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




