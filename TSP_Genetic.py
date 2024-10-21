# https://www.geeksforgeeks.org/traveling-salesman-problem-using-genetic-algorithm/
# modified to allow for different graph sizes as well as time the algorithm

from random import randint
import random
import time

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

# Maximum integer value
INT_MAX = 2147483647

# Structure of a GNOME
class individual:
    def __init__(self) -> None:
        self.gnome = ""
        self.fitness = 0

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

# Function to return a random number between start and end
def rand_num(start, end):
    return randint(start, end - 1)

# Function to check if the character has already occurred in the string
def repeat(s, ch):
    return ch in s

# Function to return a mutated GNOME by interchanging two random genes
def mutatedGene(gnome):
    gnome = list(gnome)
    while True:
        r = rand_num(1, V)
        r1 = rand_num(1, V)
        if r1 != r:
            gnome[r], gnome[r1] = gnome[r1], gnome[r]
            break
    return ''.join(gnome)

# Function to create a valid GNOME string required to create the population
def create_gnome():
    gnome = "0"  # Always start with city 0
    while len(gnome) < V:
        temp = rand_num(1, V)
        if not repeat(gnome, chr(temp + 48)):  # Ensure no city is repeated
            gnome += chr(temp + 48)
    gnome += gnome[0]  # Return to the starting city
    return gnome

# Function to return the fitness value of a gnome using the distance graph
def cal_fitness(gnome, graph):
    f = 0
    for i in range(len(gnome) - 1):
        u = ord(gnome[i]) - 48
        v = ord(gnome[i + 1]) - 48
        if graph[u][v] == INT_MAX:
            return INT_MAX  # Invalid path
        f += graph[u][v]
    return f

# Function to return the updated value of the cooling element
def cooldown(temp):
    return (90 * temp) / 100

# Utility function for TSP problem using Genetic Algorithm
def TSPUtil(graph):
    gen = 1
    gen_thres = 5
    POP_SIZE = 10  # Population size

    population = []

    # Populating the GNOME pool
    for i in range(POP_SIZE):
        temp = individual()
        temp.gnome = create_gnome()
        temp.fitness = cal_fitness(temp.gnome, graph)
        population.append(temp)

    # print("\nInitial population: \nGNOME     FITNESS VALUE\n")
    # for i in range(POP_SIZE):
    #     print(population[i].gnome, population[i].fitness)
    # print()

    temperature = 10000

    # Iteration to perform population crossing and gene mutation
    while temperature > 1000 and gen <= gen_thres:
        population.sort()
        # print("\nCurrent temp: ", temperature)
        new_population = []

        for i in range(POP_SIZE):
            p1 = population[i]

            while True:
                new_g = mutatedGene(p1.gnome)
                new_gnome = individual()
                new_gnome.gnome = new_g
                new_gnome.fitness = cal_fitness(new_gnome.gnome, graph)

                if new_gnome.fitness <= population[i].fitness:
                    new_population.append(new_gnome)
                    break
                else:
                    # Accepting rejected offspring with some probability
                    prob = pow(2.7, -1 * ((new_gnome.fitness - population[i].fitness) / temperature))
                    if prob > 0.5:
                        new_population.append(new_gnome)
                        break

        temperature = cooldown(temperature)
        population = new_population

        # print("Generation", gen)
        # print("GNOME     FITNESS VALUE")
        # for i in range(POP_SIZE):
            # print(population[i].gnome, population[i].fitness)
        # gen += 1

if __name__ == "__main__":
    # Set size of graph
    V = 16000  # Change this value to increase/decrease size

    # Generate random graph
    graph = create_graph(V)
    # v = 3
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
            # [87, 45, 5, 68, 22, 0, 59, 74, 80, 33, 36, 74, 1, 1],
            # [34, 75, 85, 51, 42, 59, 0, 66, 84, 79, 86, 21, 62, 39],
            # [1, 1, 99, 98, 9, 74, 66, 0, 68, 52, 85, 39, 63, 61],
            # [79, 16, 64, 27, 40, 80, 84, 68, 0, 31, 49, 99, 29, 27],
            # [70, 16, 26, 66, 11, 33, 79, 52, 31, 0, 53, 20, 13, 41],
            # [54, 70, 44, 73, 63, 36, 86, 85, 49, 53, 0, 33, 32, 100],
            # [25, 56, 50, 51, 44, 74, 21, 39, 99, 20, 33, 0, 48, 48],
            # [35, 42, 87, 50, 71, 1, 62, 63, 29, 13, 32, 48, 0, 63],
            # [77, 78, 23, 62, 1, 1, 39, 61, 27, 41, 100, 48, 63, 0]]


    # Print the generated graph
    # print("Generated Distance Matrix:")
    # for row in graph:
    #     print(row)

    # Start the TSP solution using Genetic Algorithm
    start_time = time.time()
    TSPUtil(graph)
    end_time = time.time()

    # Print execution time
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.4f} seconds")
    print(f"V = {V}")
