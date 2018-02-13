#!/usr/bin/env python

'''
2. 
Display an image on either the left or the right side of the screen. 

Both sides of the screen are then masked, 

Measure people's ability (e.g., accuracy, reaction time) in responding whether 
the image was on the right or left side of the screen, 

Comparing responses on masked vs. nonmasked trials.

Generate a list of trials in which some proportion is masked and some is not masked. 

Within each condition, we want the image on the left side displayed 
with some proportion of the time, and on the right the remaining times.

Begin by having 2/3 masked trials and 1/3 non-masked trials. 
Within each level of the masking factor, 
half of the targets should be on the left and half on the right. 

Let's have 5 blocks with each block having all the possible trial types.
'''


numTrials = 6 # per block 
numBlocks = 5
propMasked = 2.0/3.0
sides = ['right', 'left']



def generateTrials(numBlocks, numTrials, propMasked, sides):
	numMasked = numTrials * propMasked
	numUnMasked = numTrials - numMasked
	for b in range(numBlocks) :
		m = 1
		u = 1
		while m <= numMasked : 
			for side in sides :
				print ','.join(map(str,[b+1,'masked',side]))
				m += 1
		while u <= numUnMasked :
			for side in sides :
				print ','.join(map(str,[b+1,'nonmasked',side]))
				u += 1

generateTrials(numBlocks, numTrials, propMasked, sides)
