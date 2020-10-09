# User function Template for python3

# Complete this function
def reverseInGroups(A, N, K):
    i=0
    while(i<N):
        if(i+K<N):
            A[i:i+K] =  reversed(A[i:i+K])
            i += K
        else:
            A[i:] = reversed(A[i:])
            i += K
    return A

# Your code here


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):

        nk = [int(x) for x in input().strip().split()]

        N = nk[0]
        K = nk[1]

        A = [int(x) for x in input().strip().split()]

        A = reverseInGroups(A, N, K)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends