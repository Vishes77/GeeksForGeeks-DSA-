# User function Template for python3


# Complete this function
def maxStep(A, N):
    count = 0
    maxi = 0
    for i in range(1,N):
        count = 0
        if(A[i] < A[i-1]):
            count += 1
        else:
            maxi = max(count,maxi)
            count = 0
    maxi = max(count,maxi)

    return maxi


def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        print(maxStep(A, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends