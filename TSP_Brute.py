# Python3 program to implement traveling salesman 
# problem using naive approach. 
# Code from geeks for geeks:
#  https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
# Modified to make allow for graph to generate rather than hard coded,
# and added timing functionality for import purposes
from sys import maxsize 
from itertools import permutations
import random
import time

# Function to create graph with random distances
def create_graph(V):
   graph = [[0] * V for _ in range(V)]
   # Fill the matrix with random distances
   for i in range(V):
       for j in range(i+1, V):  # only need to fill upper triangle
           distance = random.randint(1, 100)  # random distance 1-100
           graph[i][j] = distance
           graph[j][i] = distance  # mirror it (symmetric)
   return graph

# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 
   # Check if size is too large
   if V > 11:
       print("Warning: Large V value may result in very long computation time!")

   # store all vertex apart from source vertex 
   vertex = [] 
   for i in range(V): 
       if i != s: 
           vertex.append(i) 

   # store minimum weight Hamiltonian Cycle 
   min_path = maxsize 
   next_permutation = permutations(vertex)
   for i in next_permutation:
       # store current Path weight(cost) 
       current_pathweight = 0
       # compute current path weight 
       k = s 
       for j in i: 
           current_pathweight += graph[k][j] 
           k = j 
       current_pathweight += graph[k][s] 
       # update minimum 
       min_path = min(min_path, current_pathweight) 
       
   return min_path 

# Driver Code 
if __name__ == "__main__": 
    # Set size of graph
    V = 13  # Change this value to increase/decrease size

    # Generate random graph
    graph = create_graph(V)

    # V = 5
    # graph = [[0, 87, 11, 77, 10],
    #         [87, 0, 83, 85, 91],
    #         [11, 83, 0, 44, 8],
    #         [77, 85, 44, 0, 7],
    #         [10, 91, 8, 7, 0]]
    # Print the generated graph
    print("Generated Distance Matrix:")
    for row in graph:
        print(row)

    # Set starting vertex
    s = 0

    start_time = time.time()

    # Find and print shortest path
    print("\nStarting from vertex:", s)
    print("The cost of most efficient tour =", travellingSalesmanProblem(graph, s))

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.4f} seconds")
