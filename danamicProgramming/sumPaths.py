
class FindPathToEnd(object):

    def findPathToEnd(self, grid):
        '''
        grid : 是输入的矩阵
        输出的是相应的坐标点位置， 可以转换成相应坐标值
        '''
        m = len(grid)
        n = len(grid[0]) if m else 0
        allPaths = []

        def backward(grid, i, j, path, index, temp):
            #停止条件
            if i == m - 1:
                for k in range(j, n):
                    # path[index+k-j] = (i,k)
                    path[index+k-j] = grid[i][k]
                temp.extend(path)
                allPaths.extend([temp])
                return
            if j == n - 1:
                for k in range(i, m):
                    # path[index + k - i] = (k, j)
                    path[index + k - i] = grid[k][j]

                temp.extend(path)
                allPaths.extend([temp])
                return
            # path[index] = (i,j)
            path[index] = grid[i][j]

            backward(grid, i + 1, j, path, index + 1, [])
            backward(grid, i, j + 1, path, index + 1, [])

        #path是一条路径的长度
        path = [0 for _ in range(m + n-1)]
        backward(grid, 0, 0, path, 0,[])

        return allPaths, len(allPaths)


    #若是直接想要知道总共的路径数
    #可以使用动态规划
    def numPathToend(self, grid):
        m = len(grid)
        n = len(grid[0]) if m else 0
        dp = [[1]* n] + [[1]+[0]*(n-1) for _ in range(m-1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    solu = FindPathToEnd()
    grid = [[1, 2, 3, 4],
            [5, 6, 6, 7],
            [8, 9, 10, 11]]
    allPath, numPaths = solu.findPathToEnd(grid)
    print(allPath, '\n', numPaths)

    '''
    若是坐标值，则全部路径是：
    [[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)], 
    [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (2, 3)], 
    [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)], 
    [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3)], 
    [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3)], 
    [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3)], 
    [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3)], 
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3)], 
    [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)], 
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]]
    
    若是坐标值，则全部路径是：
    [[1, 5, 8, 9, 10, 11], 
    [1, 5, 6, 9, 10, 11], 
    [1, 5, 6, 6, 10, 11], 
    [1, 5, 6, 6, 7, 11], 
    [1, 2, 6, 9, 10, 11], 
    [1, 2, 6, 6, 10, 11], 
    [1, 2, 6, 6, 7, 11], 
    [1, 2, 3, 6, 10, 11], 
    [1, 2, 3, 6, 7, 11], 
    [1, 2, 3, 4, 7, 11]] 
     
    路径总和
    10
    '''

    #单纯的使用路径规划，得出路径总和
    numPaths02 = solu.numPathToend(grid)
    print(numPaths02)






