# User function Template for python3
# We hope you are familiar with using counter variables. Counting allows us to find how may times a certain element appears in an array or list.
#
# You are given an array arr[] of size N. You are also given two elements x and y. Now, you need to tell which element (x or y) appears most in the array. In other words, return the element, x or y, that has higher frequency in the array. If both elements have the same frequency, then just return the smaller element.
#
# NOTE :  We need to return the elements, not their counts.
# Complete this function
def majorityWins(arr, n, x, y):
    i=j=0
    for k in arr:
        if k == x:
             i += 1
        elif k == y:
            j += 1
    if(i==j):
        return min(x,y)
    elif(i>j):
        return x
    else:
        return y





# code here


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    while (T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]

        x, y = map(int, input().strip().split())

        print(majorityWins(arr, n, x, y))
        T -= 1

# } Driver Code Ends