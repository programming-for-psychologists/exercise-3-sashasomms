#!/usr/bin/env python

'''
5.
Double the number of trials in each block 
(so that the repetitions are not quite so predictable), 
and then randomize within each block as in part 4.
'''

import random

numTrials = 12 # per block 
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

