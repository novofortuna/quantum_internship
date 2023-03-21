import numpy as np
from sys import setrecursionlimit
setrecursionlimit(1000000) 

def island_marker(row,column, matrix): 
    if row < 0 or row >= len(matrix) or column < 0 or column >= len(matrix[0]) or matrix[row][column] != 1:
        return 
    matrix[row][column] = 'X'
    island_marker(row - 1, column, matrix)
    island_marker(row + 1, column, matrix)
    island_marker(row, column - 1, matrix)
    island_marker(row, column + 1, matrix)

def count_islands(matrix):
    islands = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                island_marker(i, j, matrix)
                islands += 1
    return islands

def counting_islands_and_examples():
    while True:
        try:
            while True:
                M = int(input("Enter the number of rows of the matrix \n"))
                if M <= 0:
                    print("The number of rows cannot be < 0")
                else:
                    break
            break
        except ValueError:
            print("Invalid format, you need to repeat the input")

    while True:
        try:
            while True:
                N = int(input("Enter the number of columns in the matrix \n"))
                if N <= 0:
                    print("The number of columns cannot be < 0")
                else:
                    break
            break
        except ValueError:
            print("Invalid format, you need to repeat the input")

    matrix = np.random.randint(0, 2, (M, N)).tolist()
    print ("The generated matrix is randomly filled with 1 and 0")
    print(np.array(matrix))
    print("Number of islands is:", count_islands(matrix))
    print ("--------------------")

    print ("Example 1")
    matrix_exampl1 = [[0, 1, 0], [0, 0, 0], [0, 1, 1]]
    print(np.array(matrix_exampl1))
    print("Number of islands is:", count_islands(matrix_exampl1))
    print ("--------------------")

    print ("Example 2")
    matrix_exampl2 = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]]
    print(np.array(matrix_exampl2))
    print("Number of islands is:", count_islands(matrix_exampl2))
    print ("--------------------")

    print ("Example 3")
    matrix_exampl3 = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1]]
    print(np.array(matrix_exampl3))
    print("Number of islands is:", count_islands(matrix_exampl3))

if __name__ == "__main__":
    counting_islands_and_examples()