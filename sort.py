# -*- coding:utf-8 -*-
# Author : Xu MO

from typing import Optional


class Sort:

	def bubbleSort(self, arr: list, n: int):
		for i in range(len(arr)):
			flag = False
			for j in (range(0, len(arr)-i-1)):
				if arr[j] > arr[j+1]:
					tmp = arr[j]
					arr[j] = arr[j+1]
					arr[j+1] = tmp
					flag = True
			if not flag:
				break


	def selectSort(self):
		pass

	def insertSort(self, arr: list, n: int):
		arr_len = len(arr)
		for i in range(1, arr_len):
			j = i - 1
			value = arr[i]
			while j >= 0:
				if arr[j] > value:
					arr[j+1] = arr[j]
				else:
					break
				j = j - 1
			arr[j+1] = value

	def quickSort(self):
		pass


if __name__ == "__main__":
	arr = [5, 5, 6, 1, 2, 3]
	sort = Sort()
	sort.bubbleSort(arr, 6)
	print(arr)
	pass
