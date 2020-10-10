# User function Template for python3
import math
# Complete this function
def leaders(A, N):
    # Your code here
    leader = A[N-1]
    li = [leader]
    for i in range(N-2,-1,-1):
        if(A[i]>=leader):
            li.append(A[i])
            leader = A[i]
    return reversed(li)  # Time 2.94




def main():
    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]

        A = leaders(A, N)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends