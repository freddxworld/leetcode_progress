Contains Duplicates
Summary
- Given an array return true if there are any duplicate values and false if there is not
Input
- Array
Constraint
- Every value must be unique 
Base case 
- Return false if array is empty
Example
nums = [1,2,3,1]
- Looking at array we can see that there are two duplicates of 1s
Brute force 
- Do a nested loop where the outer loop Will keep track of what num were on and the inner loop will check to make sure that there are no duplicates
- O n squared for time cause of nested
- O 1 for space

Optimized
- Use hash set to keep track of duplicates
- Go through array and check if num has been seen
- O n for Time cause for loop
- O n for space cause of set 
Pattern
🔑 Hash Set Pattern (Contains Duplicate)

Goal: Detect if an array has any duplicates.
Steps:
	1.	Initialize a set to track seen elements.
	2.	Iterate through the array:
	•	If element is in the set → duplicate found → return True.
	•	Else → add element to the set.
	3.	If the loop finishes → no duplicates → return False.

Core idea:
“Use a hash set to track seen elements for O(1) lookups.”



