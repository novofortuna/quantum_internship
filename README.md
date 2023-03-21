# Quantum Data Science test task

## Task 1

A program in Python 3 that calculates the sum in range 1 and N, given N - a positive integer.

Limitations: 
* N <= 10^25;
* Execution time: 0.1 seconds.

Provided an example of a function that solves the task using the `for` loop. Not used for a final solution since it has a complexity of O(N) and don't match execution time limitations.

The final solution has a complexity of O(1) and utilizes arithmetic progression.

## Task 2

Given matrix MxN that represents a map, that can be filled with next values: 1 - islands, 0 - ocean - calculate the number of islands in the most effective way.

```
Input: 3 3
    
0 1 0
0 0 0
0 1 1

Output: 2

--------------
Input: 3 4 

0 0 0 1
0 0 1 0
0 1 0 0

Output: 3

--------------
Input: 3 4

0 0 0 1
0 0 1 1
0 1 0 1

Output: 2
```

The solution is implemented with Depth First Search (`island_marker()`) algorithm as follows:

In the function `count_islands(matrix)`, initialize `islands = 0`, to store the answer. <br>
Loop from 0 till M:<br>
&emsp; Loop from 0 to N:<br>
&emsp;&emsp; If the value of the current cell in the given matrix equals 1:<br>
&emsp;&emsp;&emsp;Call `island_marker`.<br>
&emsp;&emsp;&emsp;Increment `islands` by 1.<br>
&emsp;&emsp;&emsp;&emsp;If the cell exceeds the boundary or the value at the current cell is 0:<br>
&emsp;&emsp;&emsp;&emsp;&emsp;Return.<br>
&emsp;&emsp;&emsp;&emsp;Update the value at the current cell as 0.<br>
&emsp;&emsp;&emsp;&emsp;Call `island_marker` on the neighbor recursively. <u>NOTE: only horizontal and vertical neighbors are taken into account.</u><br>
Return `islands` as the final answer.

The final solution accepts values M and N and randomly fills the respective matrix with 0 and 1.

Additionally, the number of islands is calculated for the provided examples. 

## Task 3

### Installation

```
pip install requirements.txt
```

Files `internship_train.csv` and `internship_hidden_test.csv` should be placed in the `data` folder.

### Solution

The solution consists of two steps:
* exploratory data analysis 
* modeling and prediction

Train and test data and generated predictions are stored in the `data` folder.

At the model selection step (`task3_EDA.ipynb`), a train/test split was performed to evaluate model quality. The whole training data were used at the modeling step (`task_3.py`).

Predictions are stored to the `data/preds.csv`.
