# Two Sum
Your given an array return the index of the two nums that when added together equal to target 

## Inputs
- Array of nums
- Target value
## Constraints
- Can’t use the same elements twice
## Example
nums = [2,7,11,15], target = 9
9 - 2  = 7
Look in the array see if you can spot 7 then return the index
## Brute force
- So I would do a for loop on nums
- For each num I would subtract that from the target 
- Then I would check the array again with another for loop so a I guess a nested loop and see if that number exists 
- If it does the exit the for loop and return the indexes
O n squared for Time 
O n  for space
## Optimize 
- I would use a dict that way I could store both the num and it index that way I can go back and check fast and so I dont need to use a nested loop
## Code
unique_dic = {}
for i, num in enumerate(nums):
	complement = target - num
	if complement in unique_dic:
		return[I , unique_dic[complement]]
	unique[num] = I
	

O n time 
O n space


## Pattern
“Use a hash map to check past values quickly while scanning forward.” 
🔑 General Hashing Pattern (for Two Sum–style problems)
	•	Goal: Find pairs (or groups) of numbers that satisfy a condition (e.g., add to a target).
	•	Steps:
	1.	Use a hash map (dict) to store what you’ve seen (value → index).
	2.	For each new number, compute what you need (the complement).
	3.	Check the hash map → if it’s there, you found a solution.
	4.	Otherwise, record the current number for future checks.
