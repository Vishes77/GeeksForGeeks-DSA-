#User function Template for python3

def spirallyTraverse(matrix, r, c):
    row = 0
    col = 0
    output = []
    while (row < r and col < c):

        # Print first row
        for i in range(col, c):
            output.append(matrix[row][i])
        row += 1

        # Print last column
        for i in range(row, r):
            output.append(matrix[i][c - 1])
        c -= 1

        # Print last row
        if (row < r):
            for i in range(c - 1, (col - 1), -1):
                output.append(matrix[r - 1][i])
            r -= 1

        # Print first column
        if (col < c):
            for i in range(r - 1, row - 1, -1):
                output.append(matrix[i][col])

            col += 1

    return output

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        ans = spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends