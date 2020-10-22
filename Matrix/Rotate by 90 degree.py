# Back-end complete function Template for Python 3

# Function for do transpose of matrix
def transpose(matrix, n):
    R, C = n, n
    for i in range(R):
        for j in range(i, C):
            t = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = t

        # After transpose we swap elements of


# column one by one for finding left
# rotation of matrix by 90 degree
def reverseColumns(matrix, n):
    C = n
    R = n
    for i in range(C):
        j = 0
        k = C - 1
        while j < k:
            t = matrix[j][i]
            matrix[j][i] = matrix[k][i]
            matrix[k][i] = t
            j += 1
            k -= 1


# Function to rotate matrix anticlockwise by 90 degree
def rotateby90(a, n):
    transpose(a, n)
    reverseColumns(a, n)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = line1[k]
                k += 1

        rotateby90(matrix, n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
        print()

# } Driver Code Ends