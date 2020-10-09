# User function Template for python3


# Function to find largest and second largest element in the array
def largestAndSecondLargest(sizeOfArray, arr):
    maximun = -1
    second_maximum = -1

    for i in range(0,sizeOfArray):
        if(arr[i]>maximun):
            second_maximum = maximun
            maximun = arr[i]
        elif(arr[i]>second_maximum and arr[i] != maximun):
            second_maximum = arr[i]
    ans = [maximun,second_maximum]

    return ans


#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3

# Driver Code
def main():

    # testcase input
    testcases = int(input())

    # looping through all testcases
    while testcases > 0:

        sizeOfArray = int(input())

        arr = [int(x) for x in input().split()]

        li = largestAndSecondLargest(sizeOfArray, arr)
        for val in li:
            print(val, end = ' ')
        print('')

        testcases -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends