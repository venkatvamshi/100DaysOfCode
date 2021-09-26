# Question 1. Union of arrays

Union of two arrays can be defined as the common and distinct elements in the two arrays.
Given two sorted arrays of size n and m respectively, find their sorted union.

Example 1:

Input: 
n = 5, arr1[] = {1, 2, 3, 4, 5}  
m = 3, arr2 [] = {1, 2, 3}
Output: 1 2 3 4 5
Explanation: Distinct elements including 
both the arrays are: 1 2 3 4 5.

Expected Time Complexity: O(n+m).
Expected Auxiliary Space: O(n+m).
 
Constraints:
1 <= n, m <= 105
1 <= arr[i], brr[i] <= 106