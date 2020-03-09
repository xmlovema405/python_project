# -*- coding:utf-8 -*-
# Author : Xu MO

class Dynamic_Programming:

	# leetcode 70
	def climb_stairs(self, n: int) ->int:
		arr = [0] * (n+1)
		arr[1] = 1
		arr[2] = 2
		for i in range(3, n+1):
			arr[i] = arr[i-1] + arr[i-2]
		return arr[n]

	#leetcode 62
	def uniquePaths(self, m: int, n: int) -> int:
		if m < 0 or n < 0:
			return 0
		arr = [[0]*n]*m

		for i in range(0, n):
			arr[0][i] = 1
		for j in range(0, m):
			arr[j][0] = 1
		for i in range(1, m):
			for j in range(1, n):
				arr[i][j] = arr[i-1][j] + arr[i][j-1]
		return arr[m-1][n-1]

	#leetcode 64
	def minPathSum(self, grid: list[list[int]]) -> int:
		m = len(grid)
		n = len(grid[0])
		if m < 0 or n < 0:
			return 0
		dp = [[0] * n for i in range(m)]
		dp[0][0] = grid[0][0]
		for i in range(1, n):
			dp[0][i] = dp[0][i-1] + grid[0][i]
		for j in range(1, m):
			dp[j][0] = dp[j-1][0] + grid[j][0]
		for i in range(1, m):
			for j in range(1, m):
				dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
		return dp[m-1][n-1]




if __name__ == "__main__":
	solution = Dynamic_Programming()
	print(solution.climb_stairs(6))
	print([[0]*6]*2)
	pass
