# ref
# https://www.geeksforgeeks.org/
# https://www.tutorialspoint.com/python_data_structure/
# https://www.programiz.com/dsa/
from random import randint
from time import time
from algo import *

# define N-arrays
list_test = [10**x for x in range(1, 6)] # from 100-1.000.000
# define 3 mode
list_mode = ["Full Random", "Half Random", "Full Sorted"]

start_all = time()

# iterate each simulation
for count in range(len(list_mode)):
	for x in list_test:
		print("=="*50)
		print()
		if list_mode[count] == "Full Random":
			print("Test Case N-array size : ", x)
			a = [randint(1, x) for _ in range(x)]
			print("Full Random Mode")
		elif list_mode[count] == "Half Random":
			print("Test Case N-array size : ", x)
			a = [randint(1, x) for _ in range(x)]
			# half sort
			a_sorted = sorted(a[:int(len(a)/2)])
			# combine - half sorted & not sorted
			a = a_sorted + a[int(len(a)/2):]
			print("Half Random Mode")
		else:
			print("Test Case N-array size : ", x)
			a = sorted(randint(1, x) for _ in range(x))
			print("Full Sorted Mode")

		if len(a) < 100000:
			# algorithm sorting started - repeat
			start = time()
			bubbleSort(a)
			print("Bubble Sort Estimated Time  \t: ", time()-start)
			start = time()
			insertionSort(a)
			print("Insertion Sort Estimated Time \t: ", time()-start)
			start = time()
			selectionSort(a)
			print("Selection Sort Estimated Time \t: ", time()-start)
			start = time()
			heapSort(a)
			print("Heap Sort Estimated Time \t: ", time()-start)
			start = time()
			mergeSort(a)
			print("Merge Sort Estimated Time \t: ", time()-start)
			start = time()
			binaryTree(a)
			print("Binary Tree Estimated Time \t: ", time()-start)
			start = time()
			LLRB_tree(a)
			print("LLRB Estimated Time \t\t: ", time()-start)

			print()
			print("=="*50)
		else:
			# algorithm sorting started - repeat
			start = time()
			bubbleSort(a)
			print("Bubble Sort Estimated Time \t: ", time() - start)
			start = time()
			insertionSort(a)
			print("Insertion Sort Estimated Time \t: ", time() - start)
			start = time()
			selectionSort(a)
			print("Selection Sort Estimated Time \t: ", time() - start)
			start = time()
			heapSort(a)
			print("Heap Sort Estimated Time \t: ", time() - start)
			start = time()
			mergeSort(a)
			print("Merge Sort Estimated Time \t: ", time() - start)
			start = time()
			binaryTree(a)
			print("Binary Tree Estimated Time \t: ", time() - start)
			start = time()
			LLRB_tree(a)
			print("LLRB Estimated Time \t\t: ", time() - start)

			print()
			print("==" * 50)

print("All Test Clear Spent : ", time()-start_all)

