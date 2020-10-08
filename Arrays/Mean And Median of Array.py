# Given an array a[ ] of size N. The task is to find the median and mean of the array elements.
# Mean is average of the numbers and median is the element which is smaller than half of the elements and
# greater than remaining half.  If there are odd elements, the median is simply the middle element in the sorted array. If there are even elements, then the median is floor of average of two middle numbers in the sorted array. If mean is floating point number, then we need to print floor of it.
# Note: To find the median, you might need to sort the array. Since sorting is covered in later tracks, we have already provided the sort function to you in the code.


# {
# Driver Code Starts
# Initial Template for Python 3


import math


# } Driver Code Ends

# User function Template for python3


##Complete the below codes
def median(A, N):
    A.sort()

    if (N%2 == 0):
        return (A[N//2]+A[(N//2)-1])//2
    else:
        return A[N//2]


def mean(A, N):
    return sum(A)//N


##Your code here


# {
# Driver Code Starts.

def main():
    T = int(input())

    while (T > 0):
        N = int(input())
        a = [int(x) for x in input().strip().split()]

        print(mean(a, N), median(a, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends