'''Given a square matrix 
M
M and two indices 
(
i
,
j
)
(i,j), 
M
i
j
M 
ij
​
  is the matrix obtained by removing the 
i
t
h
i 
th
  row and the 
j
t
h
j 
th
  column of 
M
M.

Write a function named minor_matrix that accepts three arguments:

M: a square matrix
i: a non-negative integer
j: a non-negative integer
The function should return the matrix 
M
i
j
M 
ij
​
  after removing the 
i
t
h
i 
th
  row and the 
j
t
h
j 
th
  column of 
M
M. Note that we use zero-based indexing throughout. That is, if the matrix 
M
M is of dimensions 
n
×
n
n×n, then we have 
0
≤
i
,
j
≤
n
−
1
0≤i,j≤n−1.

(1) You can assume that the number of rows in 
M
M will be at least 
3
3 in each test case.

(2) You do not have to accept input from the user or print the output to the console.'''
def minor_matrix(M, i, j):
    """
    Compute the "minor matrix"

    Arguments:
        M: list of lists
        i: integer
        j: integer
    Return:
        M_ij: list of lists
    """
    return [row[:j] + row[j+1:] for k, row in enumerate(M) if k != i]