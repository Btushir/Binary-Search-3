"""
Approach 1: Find the distance of all the numbers in the array from x. then sort the distance then
first k elements are the answer, Need to store
TC: O(n) to find distance + O(log(n)) to sort + O(k) to get k.
Instead of sorting the distance array sort the given array itself and then return.
Approach 2: Heap can also be used to find top k elements
TC: n log(k) for min heap
Approach 3: Get the distance array and find the minimum distance and expand in the opposite direction using
2 pointers.
TC: O(n) to find distance + O(k) 2 pointers
Approach 4: Get the distance array and use 2 pointers one on 0th index and other on last index.
TC: O(n-k) distance could be found on the fly + O(n-k) to copy
Approach 5: binary search
Find the number. if not present, find next lower or next higher number.
Then except in the right and left direction till k numbers are found
TC: O(log(n)) + O(k), worst case: O(n) since once bianry search it done, the expanison could be all
numbers.
"""