
def frequencycount(A,N):
    # code here
    temp = (N+1)*[0]
    for i in range(N):
        temp[A[i]] += 1
    for i in range(N):
        A[i] = temp[i+1]  # method one coplexity is 3.7s
                          # method 2 4.04 complexity.
        #Alternative Method.
        # for i in range(0, N):
        #     A[i] = A[i] - 1
        #     # storing the frequency of elements using mathematical formula
        # for i in range(0, N):
        #     A[A[i] % N] = int(A[A[i] % N] + N)
        # for i in range(0, N):
        #     A[i] = int(A[i] / N)




#{
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		A=[int(x) for x in input().strip().split()]
		frequencycount(A,N)
		for i in range (len (A)):
			print(A[i], end=" ")
		print()
		T-=1



# } Driver Code Ends