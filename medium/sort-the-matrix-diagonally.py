"""
1329. Sort the Matrix Diagonally

Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

"""

"""
Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
"""

"""
Example:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

"""
import sys
import logging

class Solution(object):
    def getDiagIndex(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[List[int,int]]
        """
        #print("Processing: Matrix(%dx%d)"%(m,n))

        _list_index = []        
        for offset in range(1, n):
            _index = []
            j = 0
            for i in range((n-1-offset), n):  
                if (i==n) or (j==m):
                    break
                _index.append([j, i])
                j = j+1

            _list_index.append(_index)

        for offset in range(1, m):
            _index = []
            j = 0
            for i in range((m-1-offset), m):                
                if (i==m) or (j==n):
                    break
                _index.append([i, j])
                j = j+1

            _list_index.append(_index)

        return _list_index

    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m = len(mat)
        n = len(mat[0])


        set_list_idx = self.getDiagIndex(m, n)
           
        for list_idx in set_list_idx:
            _sel_list = []
            for idx in list_idx:
                _sel_list.append(mat[idx[0]][idx[1]])

            _sel_list.sort()

            for z, idx in enumerate(list_idx):
                mat[idx[0]][idx[1]] = _sel_list[z]
                           
        return mat
        
        
def main():

    s = Solution()

    test_cases = [[[3,3],[2,2],[1,1]], [[3,3,3],[2,2,2]], [[3,3,1,1],[2,2,1,2],[1,1,1,2]]]

    for i, test in enumerate(test_cases):
        print("[%d]"% (i + 1))
        print("Input:", test)
        print("Output:", s.diagonalSort(test))
        print('\n')

if __name__ == "__main__":
    loggerTest = logging.getLogger("test")
    loggerTest.setLevel(logging.INFO) # DEBUG < INFO < WARNING < ERROR < CRITICAL  
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    streamHander = logging.StreamHandler()
    #streamHander.setFormatter(formatter)
    loggerTest.addHandler(streamHander)

    main()    
  