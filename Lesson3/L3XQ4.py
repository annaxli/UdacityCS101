# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(puzzle):
    i = 0
    for row in puzzle: # one row in puzzle
        col = getCol(puzzle, i)
        newRow = row[i:]
        newCol = col[i:]
        if newRow != newCol:
            return False
        else:
            i += 1
    return True

def getCol(puzzle, i):
    col=[]
    for row in puzzle: 
        col.append(row[i])
    i = 0
    for digit in col: 
        col[i] = -digit
        i += 1
    return col   


# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False
