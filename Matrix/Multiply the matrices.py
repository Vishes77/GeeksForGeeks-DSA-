# User function Template for python3

def multiplyMatrix(A, B):
    n1 = len(A)
    m1 = len(A[0])
    n2 = len(B)
    m2 = len(B[0])
    result = []

    if (m1 == n2):
        result = [[0 for j in range(m2)] for i in range(n1)]
        for i in range(n1):
            for j in range(m2):
                sum = 0
                for k in range(0, m1):
                    sum += A[i][k] * B[k][j]
                result[i][j] = sum
    return result


# code here


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n1, m1 = map(int, input().strip().split())
        A = [[0 for j in range(m1)] for i in range(n1)]
        line1 = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(n1):
            for j in range(m1):
                A[i][j] = line1[k]
                k += 1

        n2, m2 = map(int, input().strip().split())
        B = [[0 for j in range(m2)] for i in range(n2)]
        line2 = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(n2):
            for j in range(m2):
                B[i][j] = line2[k]
                k += 1

        ans = multiplyMatrix(A, B)

        if (len(ans) == 0):
            print(-1)
        else:
            for i in range(len(ans)):
                for j in range(len(ans[0])):
                    print(ans[i][j], end=' ')
            print()

            # } Driver Code Ends