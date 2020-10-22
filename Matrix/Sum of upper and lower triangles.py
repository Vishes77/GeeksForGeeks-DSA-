# User function Template for python3

def sumTriangles(matrix, n):
    upper = 0
    lower = 0
    for i in range(n):
        for j in range(n):
            if(i == j):
                upper += matrix[i][j]
                lower += matrix[i][j]
            elif(j>i):
                upper += matrix[i][j]
            elif(j<i):
                lower += matrix[i][j]
    return [upper,lower]
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

        ans = sumTriangles(matrix, n)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends