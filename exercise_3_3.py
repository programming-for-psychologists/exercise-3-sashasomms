#!/usr/bin/env python

'''
3. 
Randomize trial list from #2
'''
import random

numTrials = 6 # per block 
numBlocks = 5
propMasked = 2.0/3.0
sides = ['right', 'left']


def generateTrials(numBlocks, numTrials, propMasked, sides):
	numMasked = numTrials * propMasked
	numUnMasked = numTrials - numMasked
	trials = []
	for b in range(numBlocks) :
		m = 1
		u = 1
		while m <= numMasked : 
			for side in sides :
				thisTrial = ','.join(map(str,[b+1,'masked',side]))
				trials.append(thisTrial)
				m += 1
		while u <= numUnMasked :
			for side in sides :
				thisTrial = ','.join(map(str,[b+1,'nonmasked',side]))
				trials.append(thisTrial)
				u += 1
	return trials

trialsList = generateTrials(numBlocks, numTrials, propMasked, sides)

for t in trialsList :
	randTrial = random.choice(trialsList)
	print randTrial
