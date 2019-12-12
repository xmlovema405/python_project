import sys
import os
import numpy as np
import matplotlib.pyplot as pt
import pandas as pd

class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            pass


if __name__ == '__main__':
    matrix1 = [[0] * (3 + 1) for _ in range(3 + 1)]
    matrix2 = [[0] * (3 + 1)] * 4
    print(type(matrix1))
    print(type(matrix2))
    print("hello world")

    list1 = [1, 2, 3, 4, 5]
    x = np.arange(0, 360)
    y = np.sin(x * np.pi / 180)

    pt.plot(x, y)
    pt.show()
    next = [0,1,2,3]
    print(next)

