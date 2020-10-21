
import math

from sys import stdin

# Complete this function

def findcandidate(A):
    maj_index = 0
    count = 1
    for i in range(len(A)):
        if(A[maj_index] == A[i]):
            count += 1
        else:
            count -= 1
        if(count == 0):
            maj_index = i
            count = 1
    return A[maj_index]
def ismajority(A,candidate):
    count = 0
    for i in range(len(A)):
        if(A[i] == candidate):
            count  += 1
    if(count > len(A)/2):
        return True
    else:
        return False

def majorityElement(A, N):
    candidate = findcandidate(A)

    if ismajority(A,candidate) == True:
        return candidate
    else:
        return -1


def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        print(majorityElement(A, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends