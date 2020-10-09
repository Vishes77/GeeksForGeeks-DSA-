
import math

def rotateArr(A, D, N):
    A[0:D] = reversed(A[0:D])  #here D is D-1
    A[D:N-1] = reversed(A[D:N-1]) #complexity of reversed is O(n).
    A[0:N-1] = reversed(A[0:N-1]) # Overall Complexity is O(n)+O(n)+O(n)
                                    #that is O(N)


def main():
    T = int(input())

    while (T > 0):
        nd = [int(x) for x in input().strip().split()]
        N = nd[0]
        D = nd[1]
        A = [int(x) for x in input().strip().split()]

        rotateArr(A, D, N)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends