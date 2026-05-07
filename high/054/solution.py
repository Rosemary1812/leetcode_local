# ===== 54. 螺旋矩阵 =====
# 难度: 中等
# 英文名: Spiral Matrix
# 来源: https://leetcode.cn/problems/spiral-matrix/description/
#
# 给定一个 m × n 的矩阵 matrix ，请以顺时针顺序返回矩阵中的所有元素。
#
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
# 示例 2：
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
# ---------------------------------------------------------
#
# 思路：用方向数组表示"右→下→左→上"四个方向，从左上角出发逐格前进，遇到边界或已访问格子就右转 90°，走完 m×n 步即得到螺旋顺序。
# 时间 O(m×n) / 空间 O(1)
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)


def spiralOrder(matrix):
    m, n = len(matrix), len(matrix[0])
    ans = []
    i = j = di = 0
    for _ in range(m * n):
        ans.append(matrix[i][j])
        matrix[i][j] = None
        x, y = i + DIRS[di][0], j + DIRS[di][1]
        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] is None:
            di = (di + 1) % 4
        i += DIRS[di][0]
        j += DIRS[di][1]
    return ans


print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
