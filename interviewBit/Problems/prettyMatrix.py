

#A = 4
#4 4 4 4 4 4 4 
#4 3 3 3 3 3 4 
#4 3 2 2 2 3 4 
#4 3 2 1 2 3 4 
#4 3 2 2 2 3 4 
#4 3 3 3 3 3 4 
#4 4 4 4 4 4 4 


def matrixE(A):
    rng = 2 * A - 1

    Matrix = [[0 for x in range(rng)] for y in range(rng)] 
    for i in range (rng):
        for j in range(rng):
            
            # the radius in a matrix is defined by the max of two distances x-center and y-center
            Matrix[i][j] = max(abs(i - A + 1) + 1, abs(j - A + 1) + 1)

    return Matrix

A = matrixE(4)

#print(np.matrixE(4))


print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in A]))