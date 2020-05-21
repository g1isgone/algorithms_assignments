'''
================================================================================== 
Date: 05/20/2020
================================================================================== 
Implementation of the QuickSort Algorithm that counts num comparions
with 3 different approaches to selecting pivots:
(1) First Element - default run
(2) Last Element # 'last' as second user input arg
(3) Median Of Three # 'median' as second user input arg
================================================================================== 
'''

import sys
import math 

#counts the number of comparisons done in quicksort
count_cmps = 0 
pivot_type = ""

'''
Consider the first, middle, and final elements of a given array
Choose the median of those three elements
'''
def medianOfThree(a, l, r):
 numSubPortion = r - l + 1
 mid_idx = l + math.ceil(numSubPortion/2) - 1 
 mid = a[mid_idx] 
 first = a[l]
 last = a[r]
  
 ul = [first, mid, last]
 ul.sort()
 median = ul[1]
 
 if median == first: 
  return l 
 elif median == mid: 
  return mid_idx
 else: 
  return r 

''' 
Swaps a[i] with a[j] in place
'''
def swap(a, i, j): 
 a[j], a[i] = a[i], a[j] 


'''
Partition given around the given pivotIndex and the array a
Everything to the left of the pivotIndex will be < a[pivotIndex]
Everything right of the pivotIndex will be >= a[pivotIndex]
'''
def partition(a, l, r): 
 pivot = a[l] 
 
 i = l+1 # keeps track of where the pivot should be 
 for j in range(l+1, r+1): #j goes through all the untouched, unpartitioned elements 
  if (a[j] < pivot):  
   swap(a, i, j)
   i += 1
 
 #swap the right most element of the l-partition with the pivot 
 swap(a, l, i-1)
 return i-1 #new location of pivot, the splitPoint that partitions array a 


'''
Count the number of comparisons carried out for QuickSort 
The type of QuickSort changes via pivot_type approach 
The QuickSort is done on its subportion a[l, ..., r]
'''
def countQuickSortCmps(a, l, r): 
 global count_cmps
 numSubPortion = r - l + 1
 
 #base case, no comparisons needed 
 if (numSubPortion <= 1):
  count_cmps += 0
  return 

 count_cmps += numSubPortion - 1 

 if pivot_type == "median": #approach (3)
  median_idx = medianOfThree(a, l, r)
  swap(a, l, median_idx) #swap the median with the first element to apply approach (1)
 
 if pivot_type == "last": #approach (2)
  swap(a, l, r) #swap last element with first to apply approach (1) 

 #use the first Element as the pivot  
 splitPoint = partition(a, l, r)

 #recursively call quicksort
 countQuickSortCmps(a, l, splitPoint-1) #quickSort elements left of pivot 
 countQuickSortCmps(a, splitPoint+1, r) #quickSort elements right of pivot

 return 

def main(): 
  global pivot_type 
  user_input_file = sys.argv[1] 
  f = open(user_input_file, "r") 
  unsortedNumArr = [int(num.strip()) for num in f.readlines()]
  pivot_type = sys.argv[2] or "first"
  
  countQuickSortCmps(unsortedNumArr, 0, len(unsortedNumArr)-1)
  print("Number of comparisons done for quicksort approach " + pivot_type)  
  print(count_cmps)

if __name__ == "__main__": 
  main()
