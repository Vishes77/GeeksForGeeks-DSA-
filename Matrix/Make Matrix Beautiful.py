#
# def findMinOpeartion(matrix, n):
#     # Initialize the sumRow[] and sumCol[]
#     # array to 0
#     sumRow = [0] * n
#     sumCol = [0] * n
#
#     # Calculate sumRow[] and sumCol[] array
#     for i in range(n):
#         for j in range(n):
#             sumRow[i] += matrix[i][j]
#             sumCol[j] += matrix[i][j]
#
#             # Find maximum sum value in
#     # either row or in column
#     maxSum = 0
#     for i in range(n):
#         maxSum = max(maxSum, sumRow[i])
#         maxSum = max(maxSum, sumCol[i])
#
#     count = 0
#     i = 0
#     j = 0
#     while i < n and j < n:
#
#         # Find minimum increment required
#         # in either row or column
#         diff = min(maxSum - sumRow[i],
#                    maxSum - sumCol[j])
#
#         # Add difference in corresponding
#         # cell, sumRow[] and sumCol[] array
#         matrix[i][j] += diff
#         sumRow[i] += diff
#         sumCol[j] += diff
#
#         # Update the count variable
#         count += diff
#
#         # If ith row satisfied, increment
#         # ith value for next iteration
#         if (sumRow[i] == maxSum):
#             i += 1
#
#         # If jth column satisfied, increment
#         # jth value for next iteration
#         if (sumCol[j] == maxSum):
#             j += 1
#
#     return count
#
# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         matrix = [[0 for j in range(n)] for i in range(n)]
#         line1 = [int(x) for x in input().strip().split()]
#         k = 0
#         for i in range(n):
#             for j in range (n):
#                 matrix[i][j]=line1[k]
#                 k+=1
#         print(findMinOpeartion(matrix,n))
#
#
