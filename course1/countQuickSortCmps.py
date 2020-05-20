import sys

pivot_type = "first"
count_cmps =0 

def swap(a, i, j): 
 a[j], a[i] = a[i], a[j] 

def partition(a, pivotIndex): 
 pivot = a[pivotIndex] 
 i = 1 
 for j in range(1, len(a)): 
  if (a[j] < pivot):  
   swap(a, i, j)
   i += 1
 
 #swap the right most element of the l-partition with the pivot 
 swap(a, pivotIndex, i-1)
 return i-1 

def medianOfThree(a): 
 import math 
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

def countQuickSortCmps(a): 
 global count_cmps
 #base case, no comparisons needed 
 if (len(a) <= 1):
  count_cmps += 0
  return a
 

 count_cmps += len(a) -1 
 
 #get index of pivot 
 median_idx = medianOfThree(a)
 swap(a, 0, median_idx) 
 #swap(a, 0, len(a)-1) 
 pivotIndex = 0   
 splitPoint = partition(a, pivotIndex)

 #partition 
 l = countQuickSortCmps(a[:splitPoint])
 r = countQuickSortCmps(a[splitPoint+1:])
 l.append(a[splitPoint]) 
 return l + r 

def main(): 
  user_input_file = sys.argv[1] 
  f = open(user_input_file, "r") 
  unsortedNumArr = [int(num.strip()) for num in f.readlines()]
  sortedArr = countQuickSortCmps(unsortedNumArr)
  print(count_cmps)

if __name__ == "__main__": 
  main()
