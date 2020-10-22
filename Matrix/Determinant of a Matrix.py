def getCofactor(matrix, temp, p, q, n):
    i,j = 0,0

    #Looping for each element of the matrix
    for row in range(n):
        for col in range(n):
            # copying into temp matrix only those which are not in given row or column
            if row != p and col != q:
                temp[i][j] = matrix[row][col]
                j+=1

                #Row is filled, so increase row index and reset col index
                if j==n-1:
                    j=0
                    i+=1


# return the determinant of the given matrix
def determinantOfMatrix(matrix,n):
    #initialize result
    d = 0

    # Base case : if matrix contains single element
    if n==1:
        return matrix[0][0]

    #to store cofactors
    temp = [ [0 for i in range(n)] for i in range(n)]

    # to store sign multiplier
    sign = 1

    # Iterate for each element first row
    for i in range(n):

        # getting cofactor of a[0][i]
        getCofactor(matrix, temp, 0, i, n)
        d += sign * matrix[0][i] * determinantOfMatrix(temp,n-1)

        # terms are to be added with alternate sign
        sign = -sign

    return d

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        print(determinantOfMatrix(matrix,n))
# } Driver Code Ends