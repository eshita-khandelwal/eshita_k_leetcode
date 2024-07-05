class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first search which row you want to search the binary search algo will run for rows then finally for the columns. if target is greater than the last number in the mid row then top+=1 , check if the target is less than the first number in the mid row bottom-=1. now that we got our row to search we need to search in the coloumn. apply normal binary search, to get the target

        row,col = len(matrix),len(matrix[0])
        #search for the row
        top,bottom = 0,row-1
        while top<=bottom:
            midrow = (top+bottom)//2
            if target>matrix[midrow][-1]:
                top=midrow+1
            elif target<matrix[midrow][0]:
                bottom=midrow-1
            else:
                break
        
        if top>bottom:
            return False

        finalrow = (top+bottom)//2
        l,r=0,col-1 #search within the final row that you get and among the coloumns
        while l<=r:
            mid = (l+r)//2
            if target>matrix[finalrow][mid]:
                l=mid+1
            elif target<matrix[finalrow][mid]:
                r=mid-1
            else:
                return True
        return False
