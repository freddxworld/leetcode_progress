# Top K Frequent elements
## Summary
- Given an array along with a value k return the amount of values who have the most frequent elements
##  Inputs
- Array
- Value k
## Constraints

## Brute force
- Create var mode 
- Create a linked list to store mode
- Go through array and find your first value that has the most duplicates then remove it from the possibility of it being chosen again
- Then go through again and find next value with the most duplicates 
- O n for Time
- O n for space

## Opitimze
- This is just an idea 
- i was also thinking of usning a hash dic to keep track of the numbers with seen[num] = how many times its beetn seen and at the end go through this and look for the top k


