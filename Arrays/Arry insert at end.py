#Insertion is a basic but frequently used operation. Arrays in most languages can not be dynamically shrinked or
# expanded. Here, we will work with such arrays and try to insert an element at the end of the array.
# ou are given an array arr. The size of the array is given by sizeOfArray.
# You need to insert an element at the end.

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

# You only need to insert the given element at
# the end, i.e., at index sizeOfArray - 1. You may
# assume that the array already has sizeOfArray - 1
# elements.
def insertAtEnd(arr, sizeOfArray, element):
    arr.append(element)
    #the complexity of append is O(1).

def main():
    testcases = int(input())

    while (testcases > 0):
        sizeOfArray = int(input())

        arr = [int(x) for x in input().strip().split()]

        element = int(input())

        insertAtEnd(arr, sizeOfArray, element)

        for i in arr:
            print(i, end=" ")
        print()

        testcases -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends



