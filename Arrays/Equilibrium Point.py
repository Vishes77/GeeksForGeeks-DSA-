# User function Template for python3

# Complete this function
import math

def equilibriumPoint(A, N):
    total = sum(A)
    left_sum = 0
    right_sum = total
    if (N == 1):
        return 1

    else:
        for i in range(N):
            right_sum = right_sum - A[i]
            if (left_sum == right_sum):
                return i + 1
            left_sum = A[i] + left_sum
    return -1



def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]

        print(equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends