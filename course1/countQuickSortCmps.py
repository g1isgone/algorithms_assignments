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
def medianOfThree(a): 
 mid_idx = math.ceil(len(a)/2) -1 
 mid = a[mid_idx] 
 first = a[0]
 last = a[len(a)-1]
 
 ul = [first, mid, last]
 ul.sort()
 median = ul[1]

 if median == first: 
  return 0
 elif median == mid: 
  return mid_idx
 else: 
  return len(a)-1 

''' 
Swap values given array 'a' and  
i, j - indices of the values to swap
'''
def swap(a, i, j): 
 a[j], a[i] = a[i], a[j] 


'''
Partition given around the given pivotIndex and the array a
Everything to the left of the pivotIndex will be < a[pivotIndex]
Everything right of the pivotIndex will be >= a[pivotIndex]
'''
def partition(a, pivotIndex): 
 pivot = a[pivotIndex] 
 i = 1 # keeps track of where the pivot should be 
 for j in range(1, len(a)): #j goes through all the untouched, unpartitioned elements 
  if (a[j] < pivot):  
   swap(a, i, j)
   i += 1
 
 #swap the right most element of the l-partition with the pivot 
 swap(a, pivotIndex, i-1)
 return i-1 

def countQuickSortCmps(a): 
 global count_cmps

 #base case, no comparisons needed 
 if (len(a) <= 1):
  count_cmps += 0
  return a

 count_cmps += len(a) -1 

 if pivot_type == "median": #approach (3)
  median_idx = medianOfThree(a)
  swap(a, 0, median_idx) #swap the median with the first element to apply approach (1)
 
 elif pivot_type == "last": #approach (2)
  swap(a, 0, len(a)-1) #swap last element with first to apply approach (1) 

 #use the first Element as the pivot  
 pivotIndex = 0   
 splitPoint = partition(a, pivotIndex)

 #recursively call quicksort
 l = countQuickSortCmps(a[:splitPoint])
 r = countQuickSortCmps(a[splitPoint+1:])
 l.append(a[splitPoint]) 
 return l + r 

def main(): 
  global pivot_type 
  user_input_file = sys.argv[1] 
  f = open(user_input_file, "r") 
  unsortedNumArr = [int(num.strip()) for num in f.readlines()]
  pivot_type = sys.argv[2] 
  sortedArr = countQuickSortCmps(unsortedNumArr)
  print(count_cmps)

if __name__ == "__main__": 
  main()
