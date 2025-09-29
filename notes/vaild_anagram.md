# Valid Anagram
## summary
Were given go strings check if the first string can be rearranged to make the second string

## input 
- Two strings

## Base Case
- If Both strings do not have the same amount of chars then we know that they are not an anagram

## Brute force
- Maybe do nested loop and compare each array doing this method
On squaed for the nested 
O1 space complicity 

## Optimize
- First set base case to take care of strings with different lengths
- Then for first string put occuances for all chars in dic 
- Then for the second string do another for loop but this time you will decrement those occurances from the dic

## 🔑 General Pattern: Frequency Counter
	•	Goal: Compare collections of elements (strings, arrays) by how often items occur.
	•	Steps:
	1.	If sizes differ → not equal (early return).
	2.	Use a hash map (dict) or Counter to count frequency of each element in the first collection.
	3.	Traverse the second collection:
	•	Subtract counts for each element.
	•	If an element doesn’t exist in the map (or count goes negative), return false.
	4.	At the end, all counts should be zero → valid match.

