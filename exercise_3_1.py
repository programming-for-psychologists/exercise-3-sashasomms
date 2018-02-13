#!/usr/bin/env python

'''
1. Write a function called repetition which takes three arguments: 
letters (a list), 
numberBeforeSwitch (an integer), 
and numRepetitions (also an integer). 
The function should produce a sequences of letters, 
one per line, such that calls to repetition with various parameters, 
generate the following outputs. 
(Note: There are built in functions that can do this. 
Please do not use them for the exercise).
'''

letters = ['A','B','C']
numberBeforeSwitch = int(2) # repeat letter
numRepetitions = int(1) # times to loop 



def repetition(letters, numberBeforeSwitch, numRepetitions):
	for r in range(numRepetitions) :
		for letter in letters :
			for l in range(numberBeforeSwitch) : 
				print(letter)


repetition(letters, numberBeforeSwitch, numRepetitions)
