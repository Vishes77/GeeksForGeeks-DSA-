def exchangeColumns(matrix):
    n1 = len(matrix)
    m1 = len(matrix[0])
    for i in range(n1):
        temp = matrix[i][0]
        matrix[i][0] = matrix[i][m1 - 1]
        matrix[i][m1 - 1] = temp


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(values[k])
                k += 1
            matrix.append(row)

        exchangeColumns(matrix)

        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
        print()

# } Driver Code Ends