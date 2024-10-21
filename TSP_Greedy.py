# Code from geeks for geeks:
# https://www.geeksforgeeks.org/travelling-salesman-problem-greedy-approach/
# Modified to make allow for graph to generate rather than hard coded,
# and added timing functionality for import purposes
from typing import DefaultDict
import random
import time

INT_MAX = 2147483647

# Function to create graph with random distances
def create_graph(V):
    graph = [[0] * V for _ in range(V)]
    # Fill the matrix with random distances
    for i in range(V):
        for j in range(i + 1, V):  # only need to fill upper triangle
            distance = random.randint(1, 100)  # random distance 1-100
            graph[i][j] = distance
            graph[j][i] = distance  # mirror it (symmetric)
    return graph

# Greedy TSP algorithm
def findMinRoute(tsp):
    sum = 0
    counter = 0
    j = 0
    i = 0
    min = INT_MAX
    visitedRouteList = DefaultDict(int)

    # Start from the first city (index 0)
    visitedRouteList[0] = 1
    route = [0] * len(tsp)

    # Traverse the graph matrix tsp[][]
    while i < len(tsp) and j < len(tsp[i]):

        # If we visited all cities, break the loop
        if counter >= len(tsp[i]) - 1:
            break

        # Find the unvisited city with the smallest path
        if j != i and (visitedRouteList[j] == 0):
            if tsp[i][j] < min:
                min = tsp[i][j]
                route[counter] = j + 1

        j += 1

        # Check all paths from the ith city
        if j == len(tsp[i]):
            sum += min
            min = INT_MAX
            visitedRouteList[route[counter] - 1] = 1
            j = 0
            i = route[counter] - 1
            counter += 1

    # Add cost of returning to the starting city
    i = route[counter - 1] - 1
    for j in range(len(tsp)):
        if (i != j) and tsp[i][j] < min:
            min = tsp[i][j]
            route[counter] = j + 1

    sum += min

    # Print the result
    print("Minimum Cost is :", sum)

# Driver Code
if __name__ == "__main__":
    # Set the size of the graph (number of cities)
    V = 16000  # You can change this to test larger or smaller graphs

    # Generate a random graph with V cities
    graph = create_graph(V)
    # graph = [[0, 97, 48],
    #         [97, 0, 59],
    #         [48, 59, 0]]

    # V = 5
    # graph = [[0, 87, 11, 77, 10],
    #         [87, 0, 83, 85, 91],
    #         [11, 83, 0, 44, 8],
    #         [77, 85, 44, 0, 7],
    #         [10, 91, 8, 7, 0]]

    # V = 7
    # graph = [[0, 24, 58, 95, 88, 14, 82],
    #         [24, 0, 54, 51, 40, 29, 59],
    #         [58, 54, 0, 97, 88, 38, 10],
    #         [95, 51, 97, 0, 96, 98, 33],
    #         [88, 40, 88, 96, 0, 32, 31],
    #         [14, 29, 38, 98, 32, 0, 83],
    #         [82, 59, 10, 33, 31, 83, 0]]
    
    # V = 10
    # graph = [[0, 83, 41, 34, 62, 58, 35, 59, 38, 26],
    #     [83, 0, 30, 37, 16, 94, 64, 56, 84, 50],
    #     [41, 30, 0, 5, 98, 30, 84, 59, 4, 40],
    #     [34, 37, 5, 0, 32, 38, 82, 16, 78, 80],
    #     [62, 16, 98, 32, 0, 39, 29, 57, 35, 81],
    #     [58, 94, 30, 38, 39, 0, 19, 41, 58, 82],
    #     [35, 64, 84, 82, 29, 19, 0, 64, 77, 42],
    #     [59, 56, 59, 16, 57, 41, 64, 0, 20, 73],
    #     [38, 84, 4, 78, 35, 58, 77, 20, 0, 10],
    #     [26, 50, 40, 80, 81, 82, 42, 73, 10, 0]]

    # V = 13
    # graph = [[0, 12, 66, 22, 100, 9, 57, 4, 28, 60, 34, 25, 81],
    #         [12, 0, 30, 44, 33, 67, 3, 98, 99, 9, 22, 16, 59],
    #         [66, 30, 0, 78, 53, 5, 43, 63, 28, 25, 7, 74, 7],
    #         [22, 44, 78, 0, 37, 51, 30, 79, 51, 14, 16, 66, 74],
    #         [100, 33, 53, 37, 0, 81, 93, 19, 84, 93, 90, 16, 26],
    #         [9, 67, 5, 51, 81, 0, 92, 66, 26, 86, 75, 5, 95],
    #         [57, 3, 43, 30, 93, 92, 0, 90, 32, 33, 59, 59, 17],
    #         [4, 98, 63, 79, 19, 66, 90, 0, 41, 44, 28, 62, 89],
    #         [28, 99, 28, 51, 84, 26, 32, 41, 0, 34, 52, 75, 60],
    #         [60, 9, 25, 14, 93, 86, 33, 44, 34, 0, 16, 35, 70],
    #         [34, 22, 7, 16, 90, 75, 59, 28, 52, 16, 0, 92, 43],
    #         [25, 16, 74, 66, 16, 5, 59, 62, 75, 35, 92, 0, 20],
    #         [81, 59, 7, 74, 26, 95, 17, 89, 60, 70, 43, 20, 0]]

    # V = 14
    # graph = [[0, 31, 72, 41, 17, 87, 34, 1, 79, 70, 54, 25, 35, 77],
    #         [31, 0, 21, 5, 67, 45, 75, 1, 16, 16, 70, 56, 42, 78],
    #         [72, 21, 0, 45, 6, 5, 85, 99, 64, 26, 44, 50, 87, 23],
    #         [41, 5, 45, 0, 75, 68, 51, 98, 27, 66, 73, 51, 50, 62],
    #         [17, 67, 6, 75, 0, 22, 42, 9, 40, 11, 63, 44, 71, 1],
    #         [87, 45, 5, 68, 22, 0, 59, 74, 80, 33, 36, 74, 1, 1],
    #         [34, 75, 85, 51, 42, 59, 0, 66, 84, 79, 86, 21, 62, 39],
    #         [1, 1, 99, 98, 9, 74, 66, 0, 68, 52, 85, 39, 63, 61],
    #         [79, 16, 64, 27, 40, 80, 84, 68, 0, 31, 49, 99, 29, 27],
    #         [70, 16, 26, 66, 11, 33, 79, 52, 31, 0, 53, 20, 13, 41],
    #         [54, 70, 44, 73, 63, 36, 86, 85, 49, 53, 0, 33, 32, 100],
    #         [25, 56, 50, 51, 44, 74, 21, 39, 99, 20, 33, 0, 48, 48],
    #         [35, 42, 87, 50, 71, 1, 62, 63, 29, 13, 32, 48, 0, 63],
    #         [77, 78, 23, 62, 1, 1, 39, 61, 27, 41, 100, 48, 63, 0]]

    # Print the generated distance matrix
    # print("Generated Distance Matrix:")
    # for row in graph:
    #     print(row)

    # Time the execution of the greedy TSP algorithm
    start_time = time.time()
    findMinRoute(graph)
    end_time = time.time()

    # Print the execution time
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.4f} seconds")
    print(f"V = {V}")
