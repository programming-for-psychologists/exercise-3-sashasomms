#!/usr/bin/env python

'''
4.
Simply randomizing the entire list messes up the block structure creating the 
possibility that participants will see the same trial multiple times in a row. 
For this part, randomize the trials within each block before printing the list.
'''
import random

numTrials = 6 # per block 
numBlocks = 5
propMasked = 2.0/3.0
sides = ['right', 'left']


def generateTrials(numBlocks, numTrials, propMasked, sides):
	numMasked = numTrials * propMasked
	numUnMasked = numTrials - numMasked
	# entire trial list
	trials = []
	for b in range(numBlocks) :
		# this block's trials
		trialsB = []
		m = 1
		u = 1
		while m <= numMasked : 
			for side in sides :
				thisTrial = ','.join(map(str,[b+1,'masked',side]))
				trialsB.append(thisTrial)
				m += 1
		while u <= numUnMasked :
			for side in sides :
				thisTrial = ','.join(map(str,[b+1,'nonmasked',side]))
				trialsB.append(thisTrial)
				u += 1
		random.shuffle(trialsB)
		trials.extend(trialsB)
	return trials

trialsList = generateTrials(numBlocks, numTrials, propMasked, sides)

for t in trialsList :
	print t

