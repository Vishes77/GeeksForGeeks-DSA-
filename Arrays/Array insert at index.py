# User function Template for python3

'''You need to insert the given element at the given index.
After inserting the elements at index, elements
from index onward should be shifted one position ahead
 You may assume that the array already has sizeOfArray - 1
elements.'''


def insertAtIndex(arr, sizeOfArray, index, element):
    # First Approach is very simple
    # arr.insert(index,element) #has O(N) - complexity.
    # else go with the down solution.
    if(index == sizeOfArray-1):
        arr[index] = element
        return
    else:
        arr[sizeOfArray - 1] = -1
        for i in range(sizeOfArray - 1, index, -1):
            temp = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = temp

        arr[index] = element




def main():
    T = int(input())
    while (T > 0):
        sizeOfArray = int(input())
        arr = [int(x) for x in input().strip().split()]
        arr.append(-1)
        index, element = map(int, input().strip().split())

        insertAtIndex(arr, sizeOfArray, index, element)

        for i in range(sizeOfArray):
            print(arr[i], end=" ")
        print()
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends