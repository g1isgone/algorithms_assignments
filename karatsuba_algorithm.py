'''
================================================================================== 
Date: 05/02/2020
================================================================================== 
Implementation of the Karatsuba algorithm
Practice of a divide and conquer approach
================================================================================== 
'''

import sys
from math import ceil

'''
A fast multiplication algorithm of two n-digit numbers
'''
def karatsuba(num1, num2):
  num_digits_num1 = len(str(num1)) 
  num_digits_num2 = len(str(num2))   
  
  #================================================================================== 
  #BASE CASE 
  #================================================================================== 
  # x,y are base elements "divided" or split into the most rudimentary base elements
  # now we must "combine" these into one product 
  #================================================================================== 
  if num_digits_num1 == 1  and num_digits_num2 == 1: 
    return num1*num2 
   
  max_num_digits = max(num_digits_num1, num_digits_num2)  
  half_num_digits = ceil(max_num_digits/2) #ceil for max_num_digits is odd  
  halfway_divisor = 10**(half_num_digits)   
 
  #split the digit sequences at the center  
  a = num1 // halfway_divisor 
  b = num1 % halfway_divisor 
  c = num2 // halfway_divisor 
  d = num2 % halfway_divisor   
 
  #================================================================================== 
  #RECURSIVE STEPS 
  #================================================================================== 
  # to find the products ac and bd by calling karatsuba recursively 
  # this will further split the factors a,b,c,d til it reaches the base case
  # especially helpful incases where the num digits is still large
  #================================================================================== 
  ac = karatsuba(a,c) 
  bd = karatsuba(b,d) 
  sum_ad_bc = karatsuba(a+b, c+d) - ac - bd 
 
  return ac * 10**(2*half_num_digits) + bd + sum_ad_bc * 10**(half_num_digits)

def main(): 
  user_inputs = sys.argv 
  
  if len(user_inputs) < 3: 
    raise Exception("You need at least 2 numbers to multiply for the Karatsuba algorithm")
  if len(user_inputs) > 3:
    raise Exception("You can only multiply 2 numbers using this algorithm")  
  
  if(len(user_inputs[1]) != len(user_inputs[2])): 
    raise Exception("The length of num1 and num2 must have the same number of digits") 
  
  num1 = int(user_inputs[1])
  num2 = int(user_inputs[2]) 
  print("The user input numbers given: "+ user_inputs[1] +", " + user_inputs[2])

  product = karatsuba(num1, num2) 
  print("This is the product: " + str(product))

if __name__ == "__main__":
  main()
