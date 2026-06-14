# Brute Force sol
# TC=O(N**2)  SC=O(N**2)
"""def rotate(matrix):
    n=len(matrix)
    result=[[0]*n for _ in range(n)]
    col=n    
    for i in range(n):
        for j in range(n):
            result[j][col-1]=matrix[i][j]
        col-=1   
    return result
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))"""

# Optimal sol- Transpose then reverse each row
# TC=O(n*n)+O(n*n) ~ O(n*n)   SC=O(1)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n-1):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
