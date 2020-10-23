

def booleanMatrix(matrix):
    R = len(matrix)
    C = len(matrix[0])
    row = [0] * R
    col = [0] * C

    for i in range(0, R):
        for j in range(0, C):
            if (matrix[i][j] == 1):
                row[i] = 1
                col[j] = 1

    for i in range(0, R):
        for j in range(0, C):
            if (row[i] == 1 or col[j] == 1):
                matrix[i][j] = 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends