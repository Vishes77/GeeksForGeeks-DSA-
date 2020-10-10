# User function Template for python3
import math

def convertToWave(A, N): #logic is to swap even with odd index elements.
    for i in range(1,N,2):
        if(A[i]>A[i-1]):
            temp = A[i]
            A[i] = A[i-1]
            A[i-1] = temp

def main():
    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().split()]
        convertToWave(A, N)
        for i in A:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends