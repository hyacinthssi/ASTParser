from Scanner import *

class LexerError(Exception): pass

#Token
class Token:

	def __init__(self, startChar):

		self.cargo     = startChar.cargo

		
		# The token picks up information
		# about its location in the textFile
		self.textFile = startChar.textFile
		self.lineIndex  = startChar.lineIndex
		self.colIndex   = startChar.colIndex

		
		# When we start, the token.type is None (aka null) because
		# we won't know what kind of token we have until we have
		# finished processing all of the characters in the token.
		self.type      = None

	
	#  return a displayable string representation of the token
	def show(self,showLineNumbers=False,**kwargs):
		"""
		align=True shows token type left justified with dot leaders.
		Specify align=False to turn this feature OFF.		
		"""
		align = kwargs.get("align",True)
		if align: 
			tokenTypeLen = 12
			space = " "
		else: 
			tokenTypeLen = 0
			space = ""
			
		if showLineNumbers:
			s = str(self.lineIndex).rjust(6) + str(self.colIndex).rjust(4) + "  "
		else:
			s = ""
			
		if self.type == self.cargo: 
			s = "\t" + "Symbol" + ":" + space + self.type
		elif self.type == "Whitespace": 
			s = "\t" + "Whitespace" + ":" + space + repr(self.cargo)
		else:
			s = "\t" + self.type  + ":" + space + self.cargo
		return s
			
	guts = property(show)

	def abort(self,msg):
		lines = self.textFile.split("\n")
		sourceLine = lines[self.lineIndex]
		raise LexerError("\nIn line "      + str(self.lineIndex + 1)
			   + " near column " + str(self.colIndex + 1) + ":\n\n"
			   + sourceLine.replace("\t"," ") + "\n"
			   + " "* self.colIndex
			   + "^\n\n"
			   + msg)