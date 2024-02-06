# Sairaj_Structify
Structify take home assesment

# Python
Python=3.11.5

## Problem Statement
Find number of interesecting chords in a circle.

## Solution Analysis
Constraints: identifiers must be of format, for starting points as 's_k', k denoting the integere eg. 1,2,3 etc.
for ending points as 'e_k', k denoting the integere eg. 1,2,3 etc. Inuts must be sorted in ascending order

### Time Complexity
Worse Case: O(n)

### Working

Input is parsed to generate a dictionary, with keys denoting the chord number and values having a list of start value at index 0 and end value at index 1

An events list is initialized which keeps track of the start/end values, their index in the chords dict, and a tag(start/end). The events list is built from the the already the sorted input.

We iterate throught the events list, check whether the current element is a starting element or not, we check if it intersects with one of the previous active chords if it does we increment the interesections counter, so for all adjacent starting points, the previous starting point is present as the active chord, so incase the current chord does satisfy the condition of interesection it is accounted for. If a end point is encountered that particular active chord is terminated, handling non intersections.
