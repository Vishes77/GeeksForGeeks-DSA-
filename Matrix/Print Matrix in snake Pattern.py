#User function Template for python3

def snakePattern(matrix):
    n = len(matrix)
    output = []

    # Traverse through all rows
    for i in range(n):

        # If current row is even,
        # print from left to right
        if i % 2 == 0:
            for j in range(n):
                output.append(matrix[i][j])

        # If current row is odd,
        # print from right to left
        else:
            for j in range(n - 1, -1, -1):
                output.append(matrix[i][j])

    return output

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
        ans = snakePattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends