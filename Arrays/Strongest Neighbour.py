# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

# Function to find maximum of all adjacents
def maximumAdjacent(sizeOfArray, arr):
    for i in range(1,sizeOfArray):
        if(arr[i]>=arr[i-1]):
            print(arr[i], end =" ")
        else:
            print(arr[i-1],end = " ")
# {
# Driver Code Starts.

# Driver Code
def main():
    # testcase input
    testcases = int(input())

    # looping through all testcases
    while testcases > 0:
        sizeOfArray = int(input())

        arr = [int(x) for x in input().split()]

        maximumAdjacent(sizeOfArray, arr)

        print()

        testcases -= 1


if __name__ == '__main__':
    main()

# } Driver Code Ends