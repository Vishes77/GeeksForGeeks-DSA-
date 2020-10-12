#User function Template for python3
import atexit
import io
import sys

##Complete this function
def checkRotatedAndSorted(arr,n):
    

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        if checkRotatedAndSorted(a,n) or checkRotatedAndSorted(a[::-1],n):
            print("Yes")
        else:
            print("No")

# } Driver Code Ends