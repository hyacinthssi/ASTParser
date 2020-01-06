from Character import *

"""
A Scanner object reads through the textFile
and returns one character at a time.
"""

def initialize(textFileArg):
	global textFile, lastIndex, sourceIndex, lineIndex, colIndex
	textFile = textFileArg
	lastIndex    = len(textFile) - 1
	sourceIndex  = -1
	lineIndex    =  0
	colIndex     = -1

#-------------------------------------------------------------------
def get():
	"""
	Return the next character in textFile.
	"""
	global lastIndex, sourceIndex, lineIndex, colIndex

	sourceIndex += 1    # increment the index in textFile

	# maintain the line count
	if sourceIndex > 0:
		if textFile[sourceIndex - 1] == "\n":
			
			# The previous character in textFile was a newline
			# character.  So... we're starting a new line.
			# Increment lineIndex and reset colIndex.

			lineIndex +=1
			colIndex  = -1

	colIndex += 1

	if sourceIndex > lastIndex:
		# We've read past the end of textFile.
		# Return the ENDMARK character.
		char = Character(ENDMARK, lineIndex, colIndex, sourceIndex,textFile)
	else:
		c    = textFile[sourceIndex]
		char = Character(c, lineIndex, colIndex, sourceIndex, textFile)

	return char

#-------------------------------------------------------------------
def lookahead(offset=1):
	"""
	Return a string (not a Character object) containing the character
	at position:
			sourceIndex + offset
	Note that we do NOT move our current position in the textFile.
	That is,  we do NOT change the value of sourceIndex.
	"""
	index = sourceIndex + offset

	if index > lastIndex:
		# We've read past the end of textFile.
		# Return the ENDMARK character.
		return ENDMARK
	else:
		return textFile[index]