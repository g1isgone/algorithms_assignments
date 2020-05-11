'''
================================================================================== 
Date: 05/10/2020
================================================================================== 
Implementation of the Sort and Count Number of Inversions Algorithm 
Practice of a divide and conquer approach as well as a demonstration
of inversions 
================================================================================== 
'''

import sys
'''
 Merges two arrays that are each sorted and counts the number of split inversions 
 Split Inversions being how many times do you have to switch the positions or cross 
 elements in sortedLeft and sortedRight such that it creates a sortedMergedArray 
'''
def mergesortCountSplitInv(sortedLeft, sortedRight): 
  numSplitInversions = 0 
  sortedMergedArray = []
  
  i, j = 0,0  
  while i < len(sortedLeft) and j < len(sortedRight): # merge and sort until you reach the end of either arr 
    if (sortedLeft[i] <= sortedRight[j]): # no inversions 
      sortedMergedArray.append(sortedLeft[i])
      i += 1
    else: 
      sortedMergedArray.append(sortedRight[j]) 
      numSplitInversions += (len(sortedLeft) - i) # num inversions are num elements remaining in sortedLeft that are unmerged
      j += 1 
  
  # merge the remaining elements in sortedLeft   
  # at this point all values in sortedLeft are
  # smaller than that of sortedRight, so no inversions
  while i < len(sortedLeft): 
    sortedMergedArray.append(sortedLeft[i])
    i += 1    

  # merge the remaining elements in sortedRight 
  # after all smaller elements in sortedLeft are merged 
  while j < len(sortedRight): 
    sortedMergedArray.append(sortedRight[j]) 
    j += 1 
 
  return sortedMergedArray, numSplitInversions 


'''
 Sort and counts the number of inversions of an unsorted array
'''
def sortAndCountInv(numArr): 
  #================================================================================== 
  # BASE CASE 
  #================================================================================== 
  # If there is <= 1 element in the array, no need for inversions or sorting 
  #================================================================================== 
  if len(numArr) <= 1:
    return numArr, 0
  
   
  #================================================================================== 
  # DIVIDE - AND - CONQUER
  #================================================================================== 
  # DIVIDE the given numArr into 2 subproblems - recurse its left half and right half
  # Each recursion returns a sorted array and num inversions required within 
  # CONQUER combine the merge and sort the two arrays and combine all numInversions
  #================================================================================== 
  halfwayPoint = len(numArr)//2 
  sortedLeft, leftNumInversions = sortAndCountInv(numArr[:halfwayPoint]) 
  sortedRight, rightNumInversions = sortAndCountInv(numArr[halfwayPoint:])
  sortedNumArr, numSplitInversions = mergesortCountSplitInv(sortedLeft, sortedRight)
  totalNumInversions = leftNumInversions + rightNumInversions + numSplitInversions 
  
  return sortedNumArr, totalNumInversions 

def main(): 
  user_input_file = sys.argv[1] 
  f = open(user_input_file, "r") 
  unsortedNumArr = [int(num.strip()) for num in f.readlines()]
  
  sortedArr, totalNumInversions = sortAndCountInv(unsortedNumArr) 
  print("These are the total number of inversions:") 
  print(totalNumInversions) 


if __name__ == "__main__": 
  main()
