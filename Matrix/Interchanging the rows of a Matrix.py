# User function Template for python3

def interchangeRows(matrix):
    n1 = len(matrix)
    m1 = len(matrix[0])
    for i in range(n1//2):
        for j in range(m1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n1-1-i][j];
            matrix[n1-1-i][j] = temp




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n1, m1 = map(int, input().strip().split())
        matrix = [[0 for j in range(m1)] for i in range(n1)]
        line1 = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(n1):
            for j in range(m1):
                matrix[i][j] = line1[k]
                k += 1
        interchangeRows(matrix)
        for i in range(n1):
            for j in range(m1):
                print(matrix[i][j], end=" ")
        print()

# } Driver Code Ends