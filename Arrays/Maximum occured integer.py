import math

def maxOccured(L, R, N, maxx):
    i = 0
    while(i<N):
        A[L[i]] += 1
        A[R[i]+1] -= 1
        i += 1
    msum = A[0]
    ind = -1

    i=1

    while(i<=maxx):
        A[i]+=A[i-1]
        if msum < A[i]:
            msum = A[i]
            ind = i
        i += 1
    return ind



A = [0] * 1000000


def main():
    T = int(input())

    while (T > 0):
        global A
        A = [0] * 1000000

        N = int(input())

        L = [int(x) for x in input().strip().split()]
        R = [int(x) for x in input().strip().split()]

        maxx = max(R)

        print(maxOccured(L, R, N, maxx))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends