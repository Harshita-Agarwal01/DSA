class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Using sets
        # TC=O(mn)  SC=O(m+n)
        """r=len(matrix)
        c=len(matrix[0])
        rowset=set()
        colset=set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    rowset.add(i)
                    colset.add(j)
        for i in range(r):
            for j in range(c):
                 if i in rowset or j in colset:
                    matrix[i][j]=0"""

        # Optimal sol-using first row/col marker 
        # TC=O(mn)  SC=O(1)
        r=len(matrix)
        c=len(matrix[0])
        first_row_zero=False
        first_col_zero=False
        for j in range(c):
            if matrix[0][j]==0:
                first_row_zero=True
                break
        for i in range(r):
            if matrix[i][0]==0:
                first_col_zero=True
                break
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if first_row_zero:
            for j in range(c):
                matrix[0][j]=0
        if first_col_zero:
            for i in range(r):
                matrix[i][0]=0